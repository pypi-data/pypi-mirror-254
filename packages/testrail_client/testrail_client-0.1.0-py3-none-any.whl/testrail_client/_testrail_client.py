from testrail_api import TestRailAPI


class TestrailClient:
    def __init__(
        self,
        host: str = None,
        username: str = None,
        password: str = None,
        project_id: str = None,
        suite_id: str = None,
    ) -> None:
        if any(arg is None for arg in [host, username, password, project_id, suite_id]):
            raise ValueError("All parameters must have values")

        self._api = TestRailAPI(host, username, password)
        self.project_id = project_id
        self.suite_id = suite_id

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: str):
        self._project_id = project_id

    @property
    def suite_id(self):
        return self._suite_id

    @suite_id.setter
    def suite_id(self, suite_id: str):
        self._suite_id = suite_id

    def get_all_cases(self) -> dict:
        return self._api.cases.get_cases(
            project_id=self.project_id,
            suite_id=self.suite_id,
        )

    def get_all_sections(self) -> dict:
        pass

    def get_cases_in_section(self, section_id: str) -> dict:
        try:
            if not section_id:
                raise ValueError("section_id is not provided")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            return self._api.cases.get_cases(
                project_id=self.project_id,
                suite_id=self.suite_id,
                section_id=section_id,
            )

    def get_case(self, case_id: str) -> dict:
        try:
            if not case_id:
                raise ValueError("case_id is not provided")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            return self._api.cases.get_case(case_id=case_id)
