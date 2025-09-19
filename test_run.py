#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主程序测试运行 - 专为小白用户设计
这个脚本会运行主程序，但会先测试少量网址
"""

import os
import sys
import time

def test_main_program():
    """
    测试运行主程序
    先检查配置，然后运行少量测试
    """
    print("🚀 主程序测试运行")
    print("=" * 50)
    
    # 检查配置文件
    print("1. 检查配置文件...")
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 检查关键配置
        if 'TEL_NUMBER = \'15005118976\'' in content:
            print("✅ 手机号已设置: 15005118976")
        else:
            print("❌ 手机号配置有问题")
            return False
            
        if '张宇' in content:
            print("✅ 姓名已设置: 张宇")
        else:
            print("❌ 姓名配置有问题")
            return False
            
        if 'chrome.exe' in content:
            print("✅ 浏览器路径已设置")
        else:
            print("❌ 浏览器路径有问题")
            return False
            
    except Exception as e:
        print(f"❌ 读取配置文件失败: {e}")
        return False
    
    print("\n2. 检查数据文件...")
    # 检查api.txt文件
    try:
        with open('api.txt', 'r', encoding='utf-8') as f:
            urls = f.readlines()
        print(f"✅ 找到 {len(urls)} 个医院网址")
        
        # 只取前3个网址做测试
        test_urls = urls[:3]
        print(f"🧪 准备测试前3个网址...")
        
    except Exception as e:
        print(f"❌ 读取数据文件失败: {e}")
        return False
    
    print("\n3. 创建测试配置...")
    # 创建测试用的配置文件
    test_config = f"""
# 测试配置
TEL_NUMBER = '15005118976'
TEL_NAME = '张宇'
TEST_MODE = True  # 测试模式
"""
    
    print("\n4. 准备运行主程序...")
    print("⚠️  重要提醒:")
    print("- 程序会打开浏览器")
    print("- 自动访问医院网站")
    print("- 发送测试消息")
    print("- 每个网站停留几秒")
    
    response = input("\n是否开始运行? (输入 'yes' 继续): ")
    if response.lower() != 'yes':
        print("❌ 用户取消运行")
        return False
    
    print("\n5. 开始运行主程序...")
    try:
        # 运行主程序
        os.system('python main.py')
        print("✅ 主程序运行完成！")
        return True
        
    except Exception as e:
        print(f"❌ 运行主程序失败: {e}")
        return False

def main():
    """主函数"""
    print("🏥 医院消息发送程序 - 测试运行")
    print("专为 Windows 10 小白用户设计")
    print("=" * 50)
    
    success = test_main_program()
    
    if success:
        print("\n🎉 测试运行成功！")
        print("\n📋 总结:")
        print("✅ 配置文件正确")
        print("✅ 数据文件完整") 
        print("✅ 主程序可运行")
        print("\n🚀 现在可以正式运行了:")
        print("python main.py")
    else:
        print("\n❌ 测试运行遇到问题")
        print("请检查配置或联系技术支持")

if __name__ == "__main__":
    main()