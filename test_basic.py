#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基础测试脚本 - 面向小白用户的详细说明
这个脚本会测试项目的各个组件是否正常工作
"""

import sys
import importlib
import os

def test_import(module_name, description):
    """
    测试模块导入功能
    参数:
        module_name: 模块名称
        description: 模块描述
    """
    try:
        importlib.import_module(module_name)
        print(f"✅ {description}模块导入成功: {module_name}")
        return True
    except ImportError as e:
        print(f"❌ {description}模块导入失败: {module_name}")
        print(f"   错误信息: {e}")
        return False
    except Exception as e:
        print(f"❌ {description}模块导入时发生未知错误: {module_name}")
        print(f"   错误信息: {e}")
        return False

def test_file_exists(file_path, description):
    """
    测试文件是否存在
    参数:
        file_path: 文件路径
        description: 文件描述
    """
    if os.path.exists(file_path):
        print(f"✅ {description}文件存在: {file_path}")
        return True
    else:
        print(f"❌ {description}文件不存在: {file_path}")
        return False

def main():
    """
    主测试函数 - 面向小白用户的详细测试流程
    """
    print("=" * 60)
    print("项目完整性测试开始...")
    print("=" * 60)
    
    # 测试Python版本
    print(f"\n1. Python环境检查:")
    print(f"   Python版本: {sys.version}")
    if sys.version_info >= (3, 7):
        print("✅ Python版本符合要求 (3.7+)")
    else:
        print("❌ Python版本过低，需要3.7或更高版本")
        return
    
    # 测试项目文件完整性
    print(f"\n2. 项目文件完整性检查:")
    files_to_check = [
        ("main.py", "主程序"),
        ("scheduler.py", "定时任务调度器"),
        ("requirements.txt", "依赖包列表"),
        ("api.txt", "医院网址数据库"),
        ("catchad/catch.py", "爬虫程序"),
        ("catchad/kw_city", "城市关键词"),
        ("catchad/kw_hospital.txt", "医院关键词"),
        ("README.md", "项目说明文档")
    ]
    
    file_check_passed = 0
    for file_path, description in files_to_check:
        if test_file_exists(file_path, description):
            file_check_passed += 1
    
    print(f"\n   文件检查结果: {file_check_passed}/{len(files_to_check)} 个文件正常")
    
    # 测试依赖包导入
    print(f"\n3. 依赖包导入测试:")
    modules_to_test = [
        ("time", "时间处理"),
        ("random", "随机数生成"),
        ("collections", "集合工具"),
        ("concurrent.futures", "并发处理"),
        ("requests", "HTTP请求"),
        ("re", "正则表达式"),
        ("os", "操作系统接口"),
        ("sys", "系统参数"),
        ("apscheduler", "定时任务调度"),
        ("fake_useragent", "伪造用户代理"),
        ("DrissionPage", "浏览器自动化")
    ]
    
    module_check_passed = 0
    for module_name, description in modules_to_test:
        if test_import(module_name, description):
            module_check_passed += 1
    
    print(f"\n   依赖包检查结果: {module_check_passed}/{len(modules_to_test)} 个包导入正常")
    
    # 测试配置读取
    print(f"\n4. 配置文件检查:")
    try:
        # 读取requirements.txt检查依赖
        with open("requirements.txt", "r", encoding="utf-8") as f:
            requirements = f.readlines()
        
        print(f"   依赖包数量: {len(requirements)} 个")
        for req in requirements:
            req_name = req.strip().split("==")[0]
            if test_import(req_name, f"依赖包 {req_name}"):
                pass
            else:
                print(f"   ⚠️  注意: {req_name} 可能需要手动安装")
        
    except Exception as e:
        print(f"❌ 配置文件读取失败: {e}")
    
    # 测试api.txt内容
    print(f"\n5. 数据文件检查:")
    try:
        with open("api.txt", "r", encoding="utf-8") as f:
            urls = f.readlines()
        
        valid_urls = [url.strip() for url in urls if url.strip().startswith("http")]
        print(f"✅ 医院网址数据库检查正常")
        print(f"   总URL数量: {len(urls)} 个")
        print(f"   有效URL数量: {len(valid_urls)} 个")
        
        if len(valid_urls) > 0:
            print(f"   示例URL: {valid_urls[0][:50]}...")
        
    except Exception as e:
        print(f"❌ 数据文件检查失败: {e}")
    
    # 测试关键词文件
    try:
        with open("catchad/kw_city", "r", encoding="utf-8") as f:
            cities = f.readlines()
        with open("catchad/kw_hospital.txt", "r", encoding="utf-8") as f:
            hospitals = f.readlines()
        
        print(f"✅ 关键词文件检查正常")
        print(f"   城市关键词数量: {len(cities)} 个")
        print(f"   医院关键词数量: {len(hospitals)} 个")
        
    except Exception as e:
        print(f"❌ 关键词文件检查失败: {e}")
    
    # 总结
    print(f"\n" + "=" * 60)
    print("测试总结:")
    print("=" * 60)
    
    if file_check_passed == len(files_to_check) and module_check_passed >= len(modules_to_test) - 2:
        print("✅ 项目完整性检查通过！")
        print("✅ 项目可以正常运行")
        print("\n下一步操作:")
        print("1. 打开 main.py 文件")
        print("2. 设置 TEL_NUMBER 变量为你的手机号码")
        print("3. 运行: python main.py")
    else:
        print("⚠️  项目存在一些问题，建议检查:")
        if file_check_passed < len(files_to_check):
            print(f"   - 缺少文件: {len(files_to_check) - file_check_passed} 个")
        if module_check_passed < len(modules_to_test):
            print(f"   - 依赖包问题: {len(modules_to_test) - module_check_passed} 个")
        print("\n建议操作:")
        print("1. 检查文件是否完整")
        print("2. 重新安装依赖: pip install -r requirements.txt")
        print("3. 检查Python环境")

if __name__ == "__main__":
    main()