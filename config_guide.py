#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置指导脚本 - 面向小白用户的详细配置说明
这个脚本会指导你如何正确配置项目参数
"""

def show_config_guide():
    """
    显示配置指导说明
    """
    print("=" * 70)
    print("项目配置指导 - 小白用户专用")
    print("=" * 70)
    
    print("\n📋 配置步骤说明:")
    print("-" * 50)
    
    print("\n1️⃣ 第一步: 设置手机号码")
    print("   打开 main.py 文件，找到下面这一行:")
    print("   TEL_NUMBER = ''  # 13385736745")
    print("   ")
    print("   修改为你的手机号码，例如:")
    print("   TEL_NUMBER = '13800138000'  # 把号码改成你的手机号")
    print("   ")
    print("   ⚠️  注意: 号码必须是11位数字，不要加引号外面的空格")
    
    print("\n2️⃣ 第二步: 设置姓名 (可选)")
    print("   找到下面这一行:")
    print("   TEL_NAME = ''  # 名字(可选)")
    print("   ")
    print("   可以修改为你的名字或昵称，例如:")
    print("   TEL_NAME = '张先生'  # 把名字改成你想要的")
    print("   ")
    print("   如果不需要留名字，保持空字符串即可")
    
    print("\n3️⃣ 第三步: 浏览器设置 (一般不需要改)")
    print("   浏览器路径设置:")
    print("   set_paths(browser_path=r'F:\\Quark\\quark.exe')")
    print("   ")
    print("   这个路径是浏览器的安装位置，默认使用夸克浏览器")
    print("   如果你使用其他浏览器，需要修改这个路径")
    print("   ")
    print("   常用浏览器路径示例:")
    print("   - Chrome:  C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    print("   - Edge:    C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
    print("   - Firefox: C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    
    print("\n4️⃣ 第四步: 运行模式设置")
    print("   set_headless(False)  # 有界面模式")
    print("   ")
    print("   False 表示可以看到浏览器窗口运行过程")
    print("   True 表示后台运行，看不到浏览器窗口")
    print("   小白用户建议保持 False，可以看到运行过程")
    
    print("\n🔧 高级设置 (小白用户可跳过)")
    print("-" * 50)
    
    print("\n验证码功能设置:")
    print("ENABLE_OTP = False  # 如果为True ,且页面元素存在'去官网按钮'则进入官网发送验证码")
    print("   ")
    print("False 表示不启用验证码功能")
    print("True 表示启用验证码功能 (需要更多设置)")
    print("小白用户建议保持 False")
    
    print("\n📱 配置检查工具")
    print("-" * 50)
    
    print("\n配置完成后，可以运行这个检查工具:")
    print("python check_config.py")
    print("\n这个工具会检查你的配置是否正确")
    
    print("\n🚨 重要提醒")
    print("-" * 50)
    
    print("\n⚠️  使用前必须知道:")
    print("1. 本项目仅供测试和学习使用")
    print("2. 不要用于非法用途")
    print("3. 使用后24小时内删除相关内容")
    print("4. 所有后果由使用者自行承担")
    print("5. 请遵守相关法律法规")
    
    print("\n✅ 配置完成后:")
    print("1. 保存 main.py 文件")
    print("2. 运行: python main.py")
    print("3. 观察浏览器自动运行过程")
    print("4. 等待程序执行完成")
    
    print("\n❌ 常见问题:")
    print("-" * 50)
    
    print("\nQ: 运行时报错找不到浏览器？")
    print("A: 检查浏览器路径是否正确，浏览器是否已安装")
    
    print("\nQ: 运行时报错依赖包缺失？")
    print("A: 重新安装依赖: pip install -r requirements.txt")
    
    print("\nQ: 运行时没有任何反应？")
    print("A: 检查手机号码是否设置正确，是否有网络连接")
    
    print("\n📞 技术支持")
    print("-" * 50)
    
    print("\n如果遇到问题:")
    print("1. 先运行 python test_basic.py 检查项目完整性")
    print("2. 查看报错信息，对照常见问题解决")
    print("3. 检查网络连接是否正常")
    print("4. 确保浏览器可以正常打开网页")
    
    print("\n" + "=" * 70)
    print("配置指导结束，祝使用顺利！")
    print("=" * 70)

if __name__ == "__main__":
    show_config_guide()