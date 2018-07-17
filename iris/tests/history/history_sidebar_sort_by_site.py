# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.meta = 'This is a test of the sorting options from the sidebar - By Site.'

    def setup(self):
        """Test case setup

        This overrides the setup method in the BaseTest class, so that it can use a brand new profile.
        """
        BaseTest.setup(self)
        self.profile = Profile.BRAND_NEW
        return

    def run(self):
        expand_button_history_sidebar = 'expand_button_history_sidebar.png'
        history_sidebar_view_button = 'history_sidebar_view_button.png'
        history_sidebar_sort_by_date = 'history_sidebar_sort_by_date.png'
        history_sidebar_sort_by_site = 'history_sidebar_sort_by_site.png'
        history_sidebar_items_sort_by_site = 'history_sidebar_items_sort_by_site.png'

        # Open some pages to create some history.
        navigate(LocalWeb.MOZILLA_TEST_SITE)
        expected_1 = exists(LocalWeb.MOZILLA_LOGO, 10)
        assert_true(self, expected_1, 'Mozilla page loaded successfully.')

        new_tab()
        navigate(LocalWeb.MOZILLA_TEST_SITE)
        expected_2 = exists(LocalWeb.MOZILLA_LOGO, 10)
        assert_true(self, expected_2, 'Mozilla page loaded successfully.')

        new_tab()
        navigate(LocalWeb.FIREFOX_TEST_SITE)
        expected_3 = exists(LocalWeb.FIREFOX_LOGO, 10)
        assert_true(self, expected_3, 'Firefox page loaded successfully.')

        new_tab()
        navigate(LocalWeb.FOCUS_TEST_SITE)
        expected_4 = exists(LocalWeb.FOCUS_LOGO, 10)
        assert_true(self, expected_4, 'Focus page loaded successfully.')

        new_tab()
        navigate(LocalWeb.POCKET_TEST_SITE)
        expected_5 = exists(LocalWeb.POCKET_LOGO, 10)
        assert_true(self, expected_5, 'Pocket page loaded successfully.')

        # Open the History sidebar.
        history_sidebar()
        expected_6 = exists(expand_button_history_sidebar, 10)
        assert_true(self, expected_6, 'Expand history sidebar button displayed properly.')
        click(expand_button_history_sidebar)

        # Sort by date by default.
        expected_7 = exists(history_sidebar_view_button, 10)
        assert_true(self, expected_7, 'View button displayed properly.')
        click(history_sidebar_view_button)
        expected_8 = exists(history_sidebar_sort_by_date, 10)
        assert_true(self, expected_8, 'Default sorting option - sort by date - is selected properly.')

        # Sort by site.
        expected_9 = exists(history_sidebar_sort_by_site, 10)
        assert_true(self, expected_9, 'Sort by site option is displayed properly.')
        click(history_sidebar_sort_by_site)
        expected_10 = exists(history_sidebar_items_sort_by_site)
        assert_true(self, expected_10, 'History list is sorted properly by site.')
