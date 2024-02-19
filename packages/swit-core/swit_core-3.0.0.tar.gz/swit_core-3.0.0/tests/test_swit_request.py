import json  # noqa: F401
import unittest

from switcore.action.schemas import SwitRequest, UserActionType, \
    QueryResource
from tests.utils import create_submit_swit_request, create_query_swit_request, create_task_swit_request


class SwitViewResponseTest(unittest.TestCase):

    def test_swit_submit_request(self):
        swit_request: SwitRequest = create_submit_swit_request("right_panel", "test_action_id01")
        self.assertEqual(swit_request.user_action.type, UserActionType.view_actions_submit)

    def test_swit_query_request(self):
        swit_request: SwitRequest = create_query_swit_request()
        self.assertEqual(swit_request.user_action.type, UserActionType.view_actions_query)
        self.assertTrue(isinstance(swit_request.user_action.resource, QueryResource))

    def test_swit_task_request(self):
        swit_request: SwitRequest = create_task_swit_request()
        self.assertEqual(swit_request.user_action.type, UserActionType.user_commands_context_menus_task.value)
        self.assertTrue(isinstance(swit_request.user_action.resource, dict))
        assert isinstance(swit_request.user_action.resource, dict)
        self.assertTrue("id" in swit_request.user_action.resource)
        self.assertTrue("parent_task_id" in swit_request.user_action.resource)
        self.assertTrue("title" in swit_request.user_action.resource)
        self.assertTrue("status" in swit_request.user_action.resource)
        self.assertTrue("assignees" in swit_request.user_action.resource)
