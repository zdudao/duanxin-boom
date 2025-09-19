#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
浏览器路径自动检测工具 - 专为小白用户设计
这个工具会自动帮你找到电脑上安装的浏览器路径
"""

import os
import platform

def find_common_browsers():
    """
    自动检测常见浏览器路径
    返回找到的所有浏览器路径
    """
    # Windows系统常见浏览器路径列表
    common_browser_paths = [
        # Chrome 浏览器常见路径
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        
        # Edge 浏览器常见路径  
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        
        # Firefox 火狐浏览器常见路径
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
        
        # 360安全浏览器常见路径
        r"C:\Users\{}\AppData\Roaming\360se6\Application\360se.exe".format(os.getenv('USERNAME')),
        
        # QQ浏览器常见路径
        r"C:\Users\{}\AppData\Local\Tencent\QQBrowser\QQBrowser.exe".format(os.getenv('USERNAME')),
        
        # 搜狗浏览器常见路径
        r"C:\Users\{}\AppData\Local\SogouExplorer\SogouExplorer.exe".format(os.getenv('USERNAME'))
    ]
    
    found_browsers = []
    
    print("🔍 正在检测您电脑上的浏览器...")
    print("=" * 50)
    
    # 逐个检查浏览器路径是否存在
    for browser_path in common_browser_paths:
        if os.path.exists(browser_path):
            found_browsers.append(browser_path)
            print(f"✅ 找到浏览器: {browser_path}")
    
    if found_browsers:
        print("\n🎉 检测完成！找到以下浏览器:")
        print("=" * 50)
        for i, browser_path in enumerate(found_browsers, 1):
            print(f"{i}. {browser_path}")
        
        print("\n📋 使用建议:")
        print("推荐使用 Chrome 或 Edge 浏览器，兼容性最好")
        print("\n💡 复制路径方法:")
        print("1. 选中上面的完整路径（从盘符到.exe）")
        print("2. 按 Ctrl+C 复制")
        print("3. 粘贴到 main.py 文件中的 browser_path 配置处")
        
    else:
        print("❌ 未找到常见浏览器！")
        print("\n🔧 解决方案:")
        print("1. 确保您已安装 Chrome、Edge、Firefox 等浏览器")
        print("2. 如果已安装但检测不到，请手动查找:")
        print("   - 右键点击浏览器图标 → 属性 → 复制'目标'路径")
        print("3. 或者下载安装 Chrome 浏览器:")
        print("   https://www.google.com/chrome/")
    
    return found_browsers

if __name__ == "__main__":
    print("🔍 浏览器路径自动检测工具")
    print("专为 Windows 10 用户设计")
    print("=" * 50)
    
    # 检测系统版本
    system_info = platform.system() + " " + platform.release()
    print(f"系统版本: {system_info}")
    print(f"用户名称: {os.getenv('USERNAME')}")
    print("=" * 50)
    
    # 开始检测
    browsers = find_common_browsers()
    
    print("\n🚀 下一步:")
    print("1. 复制上面的浏览器路径")
    print("2. 打开 main.py 文件")
    print("3. 找到 browser_path 配置行")
    print("4. 替换为复制的路径")
    print("5. 保存文件并运行: python main.py")