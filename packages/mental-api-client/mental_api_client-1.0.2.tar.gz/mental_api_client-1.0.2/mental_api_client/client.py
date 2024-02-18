import requests
import http
import urllib.parse

from mental_api_client import api_types
from mental_api_client.exceptions import APIException

_api = requests.Session()
_api.mount("https://", requests.sessions.HTTPAdapter(pool_maxsize=128))


class TeamMentalClient:
    def __init__(self, base_url, base_api_prefix='/api/v1/'):
        self._base_url = base_url
        self._base_api_prefix = base_api_prefix

    def request(
        self,
        method,
        path,
        params=None,
        json=None,
    ):
        res = _api.request(
            method,
            urllib.parse.urljoin(self._base_url, path),
            params=params,
            json=json
        )

        if res.status_code == http.HTTPStatus.NO_CONTENT.value:
            return None

        if res.status_code >= http.HTTPStatus.BAD_REQUEST.value:
            raise APIException.from_resp(res)
        return res.json()

    ###################
    #      Team       #
    ###################

    def list_teams(self) -> list[api_types.Team]:
        res = self.request('GET', self._base_api_prefix + "team/list")
        teams = []
        for team in res:
            teams.append(api_types.Team.from_dict(team))
        return teams

    def get_team(self, name_or_id: str | int) -> api_types.Team:
        res = self.request('GET', self._base_api_prefix + f'team/{name_or_id}')
        return api_types.Team.from_dict(res)

    def delete_team(self, name: str) -> None:
        self.request('DELETE', self._base_api_prefix + f'team/{name}')

    def create_team(self, team: api_types.Team) -> api_types.Team:
        json_team = team.to_dict()
        res = self.request('POST', self._base_api_prefix + 'team', json=json_team)
        return api_types.Team.from_dict(res)

    def add_user_to_team(self, team_id: int, username: str) -> None:
        json_payload = api_types.AddUserPayload(username).to_dict()
        self.request('POST', self._base_api_prefix + f'team/{team_id}/add_user', json=json_payload)

    ###################
    #      Survey     #
    ###################
    def get_surveys_period(self, survey_edges: api_types.GetSurveyEdges) -> list[api_types.Survey]:
        json_payload = survey_edges.to_dict()
        res = self.request('POST', self._base_api_prefix + 'survey/period', json=json_payload)

        survey_list = []

        for survey in res:
            survey_list.append(api_types.Survey.from_dict(survey))
        return survey_list

    def get_survey(self, survey_id: int) -> api_types.Survey:
        res = self.request('GET', self._base_api_prefix + f'survey/{survey_id}')
        return api_types.Survey.from_dict(res)

    def delete_survey(self, survey_id: int) -> None:
        self.request('DELETE', self._base_api_prefix + f'survey/{survey_id}')

    def create_survey(self, survey: api_types.Survey) -> api_types.Survey:
        json_survey = survey.to_dict()
        res = self.request('POST', self._base_api_prefix + 'survey', json=json_survey)
        return api_types.Survey.from_dict(res)

    def end_survey(self, survey_id: int) -> None:
        self.request('POST', self._base_api_prefix + f'survey/{survey_id}/end')

    def vote_survey(self, survey_id: int, vote_survey: api_types.VoteSurveyPayload) -> None:
        json_vote_survey = vote_survey.to_dict()
        self.request('POST', self._base_api_prefix + f'survey/{survey_id}/vote', json=json_vote_survey)

    def get_active_team_surveys(self, team_name: str) -> list[api_types.Survey]:
        params = {
            'team_name': team_name
        }
        res = self.request('GET', self._base_api_prefix + 'survey/active', params=params)
        res_list = []
        for item in res:
            res_list.append(api_types.Survey.from_dict(item))
        return res_list

    def get_survey_results(self, survey_id: int) -> list[api_types.UserSurvey]:
        res = self.request('GET', self._base_api_prefix + f'survey/{survey_id}/results')
        res_list = []
        for item in res:
            res_list.append(api_types.UserSurvey.from_dict(item))
        return res_list

    ###################
    #       User      #
    ###################

    def get_user(self, username: str) -> api_types.User:
        res = self.request('GET', self._base_api_prefix + f'user/{username}')
        return api_types.User.from_dict(res)

    def delete_user(self, username: str) -> None:
        self.request('DELETE', self._base_api_prefix + f'user/{username}')

    def create_user(self, user: api_types.User) -> api_types.User:
        json_user = user.to_dict()
        res = self.request('POST', self._base_api_prefix + 'user', json=json_user)
        return api_types.User.from_dict(res)
