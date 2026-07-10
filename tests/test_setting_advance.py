from pages.common.setting_page import SettingPage

def test_switch_to_advance_tab(driver):
    """
    測試從設定頁的播放分頁，成功切換到進階分頁，並讀取儲存空間
    """
    # 這裡的初始化也要同步改成 driver
    setting_page = SettingPage(driver)

    print("\n［TEST］準備切換至進階頁籤...")
    advance_page = setting_page.switch_tab("advance")

    storage_info = advance_page.get_storage_info()
    print(f"［TEST］成功切換！抓取到的空間資訊為：{storage_info}")

    assert storage_info != "", "錯誤：抓取到的儲存空間資訊為空！"