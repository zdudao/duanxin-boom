#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置检查工具 - 检查main.py中的配置是否正确
面向小白用户的详细检查说明
"""

import re
import os

def check_main_py_config():
    """
    检查main.py文件中的配置
    """
    print("🔍 配置检查工具")
    print("=" * 50)
    
    config_file = "main.py"
    
    if not os.path.exists(config_file):
        print(f"❌ 找不到配置文件: {config_file}")
        return False
    
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        print(f"✅ 成功读取配置文件: {config_file}")
        
        # 检查手机号码配置
        print(f"\n📱 手机号码配置检查:")
        tel_pattern = r"TEL_NUMBER\s*=\s*['\"](.*?)['\"]"
        tel_match = re.search(tel_pattern, content)
        
        if tel_match:
            tel_number = tel_match.group(1)
            if tel_number:
                # 检查是否是有效的手机号码
                if len(tel_number) == 11 and tel_number.isdigit():
                    print(f"✅ 手机号码设置正确: {tel_number}")
                    print(f"   号码长度: {len(tel_number)} 位")
                    print(f"   号码格式: 全数字")
                else:
                    print(f"⚠️  手机号码格式可能有问题: {tel_number}")
                    if len(tel_number) != 11:
                        print(f"   警告: 号码长度是 {len(tel_number)} 位，应该是11位")
                    if not tel_number.isdigit():
                        print(f"   警告: 号码包含非数字字符")
            else:
                print(f"❌ 手机号码为空，请设置你的手机号码")
                print(f"   找到的配置: TEL_NUMBER = '{tel_number}'")
        else:
            print(f"❌ 找不到手机号码配置项")
        
        # 检查姓名配置
        print(f"\n👤 姓名配置检查:")
        name_pattern = r"TEL_NAME\s*=\s*['\"](.*?)['\"]"
        name_match = re.search(name_pattern, content)
        
        if name_match:
            tel_name = name_match.group(1)
            if tel_name:
                print(f"✅ 姓名已设置: {tel_name}")
            else:
                print(f"ℹ️  姓名为空 (这是允许的，可选配置)")
        else:
            print(f"❌ 找不到姓名配置项")
        
        # 检查浏览器路径
        print(f"\n🌐 浏览器路径检查:")
        browser_pattern = r"browser_path\s*=\s*['\"](.*?)['\"]"
        browser_match = re.search(browser_pattern, content)
        
        if browser_match:
            browser_path = browser_match.group(1)
            print(f"✅ 浏览器路径已设置: {browser_path}")
            
            # 检查路径是否存在
            if os.path.exists(browser_path):
                print(f"✅ 浏览器文件存在")
            else:
                print(f"⚠️  警告: 浏览器文件不存在，可能需要安装或修改路径")
                print(f"   建议路径:")
                print(f"   - Chrome: C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                print(f"   - Edge:   C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
        else:
            print(f"❌ 找不到浏览器路径配置")
        
        # 检查运行模式
        print(f"\n👁️  运行模式检查:")
        headless_pattern = r"set_headless\((.*?)\)"
        headless_match = re.search(headless_pattern, content)
        
        if headless_match:
            headless_value = headless_match.group(1)
            if headless_value.lower() == "false":
                print(f"✅ 运行模式: 有界面模式 (可以看到浏览器)")
                print(f"   适合小白用户，可以看到运行过程")
            elif headless_value.lower() == "true":
                print(f"✅ 运行模式: 无界面模式 (后台运行)")
                print(f"   看不到浏览器窗口，在后台运行")
            else:
                print(f"⚠️  运行模式设置异常: {headless_value}")
        else:
            print(f"❌ 找不到运行模式配置")
        
        # 检查验证码功能
        print(f"\n🔐 验证码功能检查:")
        otp_pattern = r"ENABLE_OTP\s*=\s*(.*?)\s*#"
        otp_match = re.search(otp_pattern, content)
        
        if otp_match:
            otp_value = otp_match.group(1)
            if otp_value.lower() == "false":
                print(f"✅ 验证码功能: 关闭")
                print(f"   适合小白用户，配置简单")
            elif otp_value.lower() == "true":
                print(f"✅ 验证码功能: 开启")
                print(f"   高级功能，需要更多配置")
            else:
                print(f"⚠️  验证码功能设置异常: {otp_value}")
        else:
            print(f"❌ 找不到验证码功能配置")
        
        # 总结
        print(f"\n" + "=" * 50)
        print("📋 配置检查总结:")
        print("=" * 50)
        
        print(f"\n✅ 配置检查完成！")
        print(f"\n下一步建议:")
        print(f"1. 如果手机号码为空，请立即设置")
        print(f"2. 如果浏览器路径有问题，请修改")
        print(f"3. 其他配置可以保持默认")
        print(f"\n配置完成后，运行: python main.py")
        
    except Exception as e:
        print(f"❌ 读取配置文件时出错: {e}")
        return False

def show_quick_setup():
    """
    显示快速设置步骤
    """
    print(f"\n⚡ 快速设置步骤:")
    print("-" * 40)
    print("1. 用记事本打开 main.py")
    print("2. 找到: TEL_NUMBER = ''")
    print("3. 改成: TEL_NUMBER = '你的手机号'")
    print("4. 保存文件")
    print("5. 运行: python check_config.py")
    print("6. 检查通过后运行: python main.py")

if __name__ == "__main__":
    check_main_py_config()
    show_quick_setup()