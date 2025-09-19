#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版运行程序 - 专为小白用户设计
这个版本会逐步显示运行过程，让你知道程序在做什么
"""

import time
import random
from collections import Counter
from DrissionPage import ChromiumPage
from fake_useragent import UserAgent

# 配置参数（直接在这里设置，简单明了）
TEL_NUMBER = '15005118976'  # 你的手机号
TEL_NAME = '张宇'  # 你的名字
BROWSER_PATH = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

print("🏥 医院消息发送程序 - 简化版")
print("=" * 50)
print(f"📱 手机号: {TEL_NUMBER}")
print(f"👤 姓名: {TEL_NAME}")
print(f"🌐 浏览器: {BROWSER_PATH}")
print("=" * 50)

def simple_test():
    """简单测试运行"""
    try:
        print("1️⃣ 正在启动浏览器...")
        
        # 创建浏览器配置
        from DrissionPage import ChromiumOptions
        co = ChromiumOptions()
        co.set_no_imgs(False)  # 加载图片
        co.set_headless(False)  # 有界面模式，可以看到浏览器
        co.set_user_agent(UserAgent().random)  # 随机UserAgent
        co.set_paths(browser_path=BROWSER_PATH)
        
        print("2️⃣ 正在创建浏览器实例...")
        page = ChromiumPage(addr_driver_opts=co)
        
        print("3️⃣ 正在打开百度页面...")
        page.get('https://www.baidu.com/')
        page.wait.load_start()
        
        print("✅ 浏览器启动成功！")
        print("🎉 程序可以正常运行！")
        
        # 等待3秒让用户看到效果
        print("⏳ 等待3秒后关闭浏览器...")
        time.sleep(3)
        
        print("4️⃣ 正在关闭浏览器...")
        page.quit()
        
        print("✅ 测试完成！")
        return True
        
    except Exception as e:
        print(f"❌ 运行出错: {e}")
        print("\n🔧 解决方法:")
        print("1. 检查浏览器路径是否正确")
        print("2. 确保浏览器已安装")
        print("3. 关闭其他浏览器窗口")
        print("4. 重新运行程序")
        return False

# 运行测试
if __name__ == '__main__':
    print("🚀 开始简单测试...")
    print("这个测试会:")
    print("- 打开你的浏览器")
    print("- 访问百度网站")
    print("- 证明程序可以正常工作")
    print()
    
    input("按回车键开始测试...")
    
    success = simple_test()
    
    if success:
        print("\n🎉 太棒了！程序可以正常运行！")
        print("\n📋 下一步:")
        print("你可以运行完整版程序: python main.py")
        print("或者继续测试其他功能")
    else:
        print("\n❌ 测试失败，请检查配置或寻求帮助")