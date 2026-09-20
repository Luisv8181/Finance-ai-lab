@echo off
REM Stocker AI Agent — Scheduled Task Runner
REM This script is called by Windows Task Scheduler.
cd /d C:\STOCKER
python run_once.py
