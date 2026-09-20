@echo off
REM Stocker AI Agent — Weekly Deep Research Runner
REM Called by Windows Task Scheduler every Sunday at 6 PM.
cd /d C:\STOCKER
python run_deep_research.py
