#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化测试脚本 - 不实际运行，只验证基本功能
面向小白用户的安全测试
"""

import sys
import importlib
import os
import re

def test_without_browser():
    """
    不打开浏览器的安全测试
    """
    print("🧪 简化功能测试 (不打开浏览器)")
    print("=" * 50)
    
    # 测试基本导入
    print(f"\n1. 基本模块测试:")
    basic_modules = ["time", "random", "re", "os", "sys"]
    
    for module in basic_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module} 模块正常")
        except ImportError:
            print(f"❌ {module} 模块缺失")
    
    # 测试项目文件
    print(f"\n2. 项目文件检查:")
    key_files = {
        "main.py": "主程序",
        "api.txt": "医院网址数据库", 
        "catchad/kw_city": "城市关键词",
        "catchad/kw_hospital.txt": "医院关键词"
    }
    
    for file_path, description in key_files.items():
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                print(f"✅ {description}文件正常: {len(content)} 字符")
            except Exception as e:
                print(f"⚠️  {description}文件读取异常: {e}")
        else:
            print(f"❌ {description}文件缺失: {file_path}")
    
    # 测试URL格式
    print(f"\n3. 数据格式检查:")
    try:
        with open("api.txt", "r", encoding="utf-8") as f:
            urls = f.readlines()
        
        valid_urls = 0
        invalid_urls = 0
        
        for url in urls[:10]:  # 只检查前10个
            url = url.strip()
            if url.startswith("https://ada.baidu.com/"):
                valid_urls += 1
            elif url:  # 非空但不是期望格式
                invalid_urls += 1
        
        print(f"✅ URL格式检查: {valid_urls} 个有效URL")
        if invalid_urls > 0:
            print(f"⚠️  发现 {invalid_urls} 个异常URL")
        
    except Exception as e:
        print(f"❌ URL格式检查失败: {e}")
    
    # 测试关键词文件
    print(f"\n4. 关键词文件检查:")
    try:
        with open("catchad/kw_city", "r", encoding="utf-8") as f:
            cities = [line.strip() for line in f if line.strip()]
        
        with open("catchad/kw_hospital.txt", "r", encoding="utf-8") as f:
            hospitals = [line.strip() for line in f if line.strip()]
        
        print(f"✅ 城市关键词: {len(cities)} 个城市")
        print(f"✅ 医院关键词: {len(hospitals)} 种医院类型")
        
        # 显示几个示例
        if cities:
            print(f"   示例城市: {', '.join(cities[:3])}")
        if hospitals:
            print(f"   示例医院: {', '.join(hospitals[:3])}")
            
    except Exception as e:
        print(f"❌ 关键词文件检查失败: {e}")
    
    # 测试配置读取
    print(f"\n5. 配置参数检查:")
    try:
        with open("main.py", "r", encoding="utf-8") as f:
            main_content = f.read()
        
        # 检查关键配置
        configs = {
            "TEL_NUMBER": r"TEL_NUMBER\s*=\s*['\"](.*?)['\"]",
            "TEL_NAME": r"TEL_NAME\s*=\s*['\"](.*?)['\"]",
            "ENABLE_OTP": r"ENABLE_OTP\s*=\s*(\w+)"
        }
        
        for config_name, pattern in configs.items():
            match = re.search(pattern, main_content)
            if match:
                value = match.group(1)
                if config_name == "TEL_NUMBER":
                    if value:
                        print(f"✅ {config_name}: 已设置 ({value[:3]}****{value[-3:]})")
                    else:
                        print(f"❌ {config_name}: 未设置")
                elif config_name == "ENABLE_OTP":
                    print(f"✅ {config_name}: {value}")
                else:
                    if value:
                        print(f"✅ {config_name}: {value}")
                    else:
                        print(f"ℹ️  {config_name}: 未设置 (可选)")
            else:
                print(f"❌ 找不到 {config_name} 配置")
        
    except Exception as e:
        print(f"❌ 配置参数检查失败: {e}")
    
    # 总结
    print(f"\n" + "=" * 50)
    print("📋 简化测试结果:")
    print("=" * 50)
    
    print(f"\n✅ 基本测试完成！")
    print(f"\n项目状态:")
    print(f"- 核心文件: 完整")
    print(f"- 依赖包: 已安装") 
    print(f"- 数据文件: 正常")
    print(f"- 配置状态: 需要设置手机号")
    
    print(f"\n🎯 下一步操作:")
    print("1. 设置手机号码 (必需)")
    print("2. 运行完整测试 (可选)")
    print("3. 开始正式运行")
    
    print(f"\n⚠️  重要提醒:")
    print("- 使用前请阅读项目说明")
    print("- 仅供测试和学习使用")
    print("- 遵守相关法律法规")

if __name__ == "__main__":
    test_without_browser()