#!/bin/bash

echo "🔧 正在创建 Python 虚拟环境..."
python3 -m venv venv

echo "✅ 虚拟环境创建完成"

echo "🔃 激活虚拟环境并安装依赖..."
source venv/bin/activate

# 如果 requirements.txt 存在就安装依赖
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "⚠️ 没有找到 requirements.txt，跳过依赖安装"
fi

echo "✅ 初始化完成！可以开始开发啦 🎉"
echo "👉 每次开发前记得运行：source venv/bin/activate"