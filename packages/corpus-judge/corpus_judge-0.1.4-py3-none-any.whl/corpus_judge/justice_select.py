import datetime
import logging
from difflib import get_close_matches
from typing import Any, NamedTuple

from dateutil.parser import parse
from sqlite_utils.db import Database, Table

from .justice_name import OpinionWriterName


class JusticeDetail(NamedTuple):
    justice_id: int | None = None
    raw_ponente: str | None = None
    designation: str | None = "J."
    per_curiam: bool = False


class CandidateJustice(NamedTuple):
    db: Database
    text: str | None = None
    date_str: str | None = None
    tablename: str = "justices"

    @property
    def valid_date(self) -> datetime.date | None:
        if not self.date_str:
            return None
        try:
            return parse(self.date_str).date()
        except Exception:
            return None

    @property
    def src(self):
        return OpinionWriterName.extract(self.text)

    @property
    def candidate(self) -> str | None:
        return self.src and self.src.writer

    @property
    def table(self) -> Table:
        res = self.db[self.tablename]
        if isinstance(res, Table):
            return res
        raise Exception("Not a valid table.")

    @property
    def rows(self) -> list[dict]:
        """When selecting a ponente or voting members, create a candidate list of
        justices based on the `valid_date`.

        Returns:
            list[dict]: Filtered list of justices
        """  # noqa: E501
        if not self.valid_date:
            return []
        criteria = "inactive_date > :date and :date > start_term"
        params = {"date": self.valid_date.isoformat()}
        results = self.table.rows_where(
            where=criteria,
            where_args=params,
            select=(
                "id, full_name, lower(last_name) surname, alias, start_term,"
                " inactive_date, chief_date"
            ),
            order_by="start_term desc",
        )
        justice_list = list(results)
        sorted_list = sorted(justice_list, key=lambda d: d["id"])
        return sorted_list

    @property
    def choice(self) -> dict | None:
        """Based on `@rows`, match the cleaned_name to either the alias
        of the justice or the justice's last name; on match, determine whether the
        designation should be 'C.J.' or 'J.'
        """  # noqa: E501
        candidate_options = []
        if not self.valid_date:
            return None

        if self.text:
            # Special rule for duplicate last names
            if "Lopez" in self.text:
                if "jhosep" in self.text.lower():
                    for candidate in self.rows:
                        if int(candidate["id"]) == 190:
                            candidate_options.append(candidate)
                elif "mario" in self.text.lower():
                    for candidate in self.rows:
                        if int(candidate["id"]) == 185:
                            candidate_options.append(candidate)

        # only proceed to add more options if special rule not met
        if not candidate_options:
            if not self.candidate:
                return None

            for candidate in self.rows:
                if candidate["alias"] and candidate["alias"] == self.candidate:
                    candidate_options.append(candidate)
                    continue
                elif candidate["surname"] == self.candidate:
                    candidate_options.append(candidate)
                    continue

        if candidate_options:
            if len(candidate_options) == 1:
                res = candidate_options[0]
                res.pop("alias")
                res["surname"] = res["surname"].title()
                res["designation"] = "J."
                if chief_date := res.get("chief_date"):
                    s = parse(chief_date).date()
                    e = parse(res["inactive_date"]).date()
                    if s < self.valid_date < e:
                        res["designation"] = "C.J."
                return res
            else:
                msg = f"Too many {candidate_options=} for {self.candidate=} on {self.valid_date=}. Consider manual intervention."  # noqa: E501
                logging.error(msg)

        if self.text:
            if matches := get_close_matches(
                self.text,
                possibilities=[row["full_name"] for row in self.rows],
                n=1,
                cutoff=0.7,
            ):
                if options := list(
                    self.db[self.tablename].rows_where(
                        "full_name = ?", where_args=(matches[0],)
                    )
                ):
                    res: dict[str, str] = {}
                    selected = options[0]
                    res["id"] = selected["id"]
                    res["surname"] = selected["last_name"]
                    res["designation"] = "J."
                    if chief_date := selected.get("chief_date"):
                        s = parse(chief_date).date()
                        e = parse(res["inactive_date"]).date()
                        if s < self.valid_date < e:
                            res["designation"] = "C.J."
                    return res

        return None

    @property
    def detail(self) -> JusticeDetail | None:
        """Get object to match fields directly

        Returns:
            JusticeDetail | None: Can subsequently be used in third-party library.
        """  # noqa: E501
        if not self.src:
            return None

        if self.src.per_curiam:
            return JusticeDetail(
                justice_id=None,
                raw_ponente=None,
                designation=None,
                per_curiam=True,
            )
        elif self.choice and self.choice.get("id", None):
            digit_id = int(self.choice["id"])
            return JusticeDetail(
                justice_id=digit_id,
                raw_ponente=self.choice["surname"],
                designation=self.choice["designation"],
                per_curiam=False,
            )
        return None

    @property
    def id(self) -> int | None:
        return self.detail.justice_id if self.detail else None

    @property
    def per_curiam(self) -> bool:
        return self.detail.per_curiam if self.detail else False

    @property
    def raw_ponente(self) -> str | None:
        return self.detail.raw_ponente if self.detail else None

    @property
    def ponencia(self) -> dict[str, Any]:
        """Produces a dict of partial fields that include the following keys:

        1. `justice_id`: int
        2. `raw_ponente`: str
        3. `per_curiam`: bool
        """
        return {
            "justice_id": self.id,
            "raw_ponente": self.raw_ponente,
            "per_curiam": self.per_curiam,
        }
