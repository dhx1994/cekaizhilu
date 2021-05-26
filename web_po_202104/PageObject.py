from web_po_202104.utils import BaseApi


class IndexPage(BaseApi):
    def own_cookies(self):
        cookies = self.driver.get_cookies()
        print(cookies)

    def options(self):
        # all_handle = self.driver.window_handles
        # if self.driver.current_window_handle != 'CDwindow-4A0CC3A6ED7832EAAF3C2D20CD463003':
        #     self.driver.switch_to.window('CDwindow-4A0CC3A6ED7832EAAF3C2D20CD463003')
        # print(self.driver.title)
        self.find(("css selector", ".index_service_cnt_itemWrap:nth-child(2) .index_service_cnt_item_title")).click()
        self.find_elem(("css selector", "#js_upload_file_input")).send_keys(
            r"C:\Users\Administrator\Desktop\平安项目\附件4：平安科技复工安排表(3).xlsx")
        filename = self.find(("css selector", "#upload_file_name")).text
        print(filename)
        assert filename == "附件4：平安科技复工安排表(3).xlsx"
