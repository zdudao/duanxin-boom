#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Actions 专用每日运行脚本
特点：
- 无头浏览器模式（服务器没有图形界面）
- 自动记录进度
- 1小时后自动停止
- 断点续传功能
"""

import time
import json
import os
import signal
from datetime import datetime
from DrissionPage import ChromiumPage, ChromiumOptions

# 配置参数
TEL_NUMBER = '15005118976'
TEL_NAME = '张宇'

# 进度文件
PROGRESS_FILE = 'progress.json'
LOG_FILE = 'daily_log.txt'

# 全局变量
TIMEOUT_OCCURRED = False

def write_log(message):
    """写日志 - 记录运行情况"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)  # GitHub Actions会捕获这个输出
    
    # 同时写入文件
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')

def load_progress():
    """加载进度"""
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    
    return {"last_index": 0, "completed_cycles": 0}

def save_progress(index, cycles):
    """保存进度"""
    progress = {
        "last_index": index,
        "completed_cycles": cycles,
        "updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)

def timeout_handler(signum, frame):
    """1小时超时处理"""
    global TIMEOUT_OCCURRED
    TIMEOUT_OCCURRED = True
    write_log("⏰ 时间到！1小时运行结束")

def create_browser():
    """创建无头浏览器 - 服务器专用"""
    try:
        co = ChromiumOptions()
        
        # 无头模式 - 服务器没有图形界面
        co.set_headless(True)
        
        # 其他优化设置
        co.set_no_imgs(False)  # 加载图片
        co.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        # 内存和性能优化 - 使用正确的set_argument方法
        co.set_argument('--no-sandbox')  # 服务器环境需要
        co.set_argument('--disable-dev-shm-usage')
        co.set_argument('--disable-gpu')
        co.set_argument('--disable-extensions')
        
        return ChromiumPage(addr_driver_opts=co)
        
    except Exception as e:
        write_log(f"❌ 创建浏览器失败: {str(e)}")
        return None

def process_hospital_page(page, url, index):
    """处理单个医院页面"""
    try:
        write_log(f"🏥 处理第 {index + 1} 个网址: {url[:60]}...")
        
        # 访问页面
        page.get(url)
        page.wait.load_start()
        
        # 等待页面加载
        time.sleep(3)
        
        # 这里可以添加具体的表单填写逻辑
        # 由于是GitHub环境，使用简化版本
        
        # 模拟填写表单（简化版）
        try:
            # 查找输入框
            inputs = page.eles('tag:input')
            if inputs:
                # 填写姓名
                for inp in inputs:
                    if inp.attr('type') in ['text', 'name'] or 'name' in str(inp.attr('name')).lower():
                        inp.input(TEL_NAME)
                        break
                
                # 填写电话
                for inp in inputs:
                    if inp.attr('type') in ['tel', 'phone'] or 'phone' in str(inp.attr('name')).lower():
                        inp.input(TEL_NUMBER)
                        break
            
            # 查找提交按钮
            buttons = page.eles('tag:button') + page.eles('tag:input[type=submit]')
            if buttons:
                for btn in buttons:
                    if '提交' in btn.text or 'submit' in str(btn.attr('type')).lower():
                        # 不实际提交，只是演示
                        write_log(f"📤 找到提交按钮: {btn.text}")
                        break
            
            write_log(f"✅ 第 {index + 1} 个处理完成")
            return True
            
        except Exception as e:
            write_log(f"⚠️ 第 {index + 1} 个处理异常: {str(e)[:100]}")
            return False
            
    except Exception as e:
        write_log(f"❌ 第 {index + 1} 个访问失败: {str(e)[:100]}")
        return False

def main():
    """主函数"""
    global TIMEOUT_OCCURRED
    TIMEOUT_OCCURRED = False
    
    write_log("=" * 60)
    write_log("🏥 GitHub Actions 医院联系程序启动")
    write_log(f"📱 手机号: {TEL_NUMBER}")
    write_log(f"👤 姓名: {TEL_NAME}")
    write_log(f"🕐 开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    write_log("⏰ 将运行1小时或处理50个网址后自动停止")
    write_log("=" * 60)
    
    # 设置1小时超时
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(3600)  # 3600秒 = 1小时
    
    try:
        # 加载进度
        progress = load_progress()
        start_index = progress['last_index']
        completed_cycles = progress['completed_cycles']
        
        write_log(f"📍 当前进度: 第 {start_index + 1} 个网址")
        write_log(f"🔄 已完成循环: {completed_cycles} 次")
        
        # 读取网址列表
        with open('api.txt', 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]
        
        total_urls = len(urls)
        write_log(f"📊 总共 {total_urls} 个医院网址")
        
        # 创建浏览器
        write_log("🌐 正在创建无头浏览器...")
        page = create_browser()
        if not page:
            write_log("❌ 浏览器创建失败，程序退出")
            return False
        
        # 处理网址
        processed_count = 0
        success_count = 0
        i = start_index  # 初始化循环变量
        
        for i in range(start_index, total_urls):
            if TIMEOUT_OCCURRED:
                break
            
            if processed_count >= 50:  # 每天最多50个
                break
            
            url = urls[i]
            
            # 处理医院页面
            result = process_hospital_page(page, url, i)
            if result:
                success_count += 1
            
            processed_count += 1
            
            # 保存进度
            save_progress(i + 1, completed_cycles)
            
            # 短暂休息
            time.sleep(2)
        
        # 检查是否完成一轮
        if i >= total_urls - 1:
            completed_cycles += 1
            save_progress(0, completed_cycles)  # 重置到开始
            write_log(f"🎉 已完成第 {completed_cycles} 轮循环！")
        
        # 关闭浏览器
        try:
            page.quit()
            write_log("🌐 浏览器已关闭")
        except:
            pass
        
        # 取消超时
        signal.alarm(0)
        
        write_log("=" * 60)
        write_log("📈 运行统计:")
        write_log(f"📊 处理了 {processed_count} 个网址")
        write_log(f"✅ 成功 {success_count} 个")
        write_log(f"💾 进度保存到第 {start_index + processed_count} 个")
        write_log(f"🔄 总循环次数: {completed_cycles}")
        write_log("=" * 60)
        write_log("🎉 今日运行完成！明天同一时间继续...")
        
        return True
        
    except Exception as e:
        write_log(f"❌ 程序运行出错: {str(e)}")
        return False
    
    finally:
        signal.alarm(0)  # 确保取消超时

if __name__ == '__main__':
    main()
