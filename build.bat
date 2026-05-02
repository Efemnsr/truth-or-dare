@echo off
echo ========================================
echo   Dogruluk mu Cesaret mi - EXE Yapici
echo ========================================
echo.

REM PyInstaller yoksa yukle
pip show pyinstaller >nul 2>&1
IF ERRORLEVEL 1 (
    echo PyInstaller yukleniyor...
    pip install pyinstaller
)

echo.
echo EXE olusturuluyor...
pyinstaller --onefile --windowed --name "DogrulukMuCesaretMi" truth_or_dare.py

echo.
IF EXIST dist\DogrulukMuCesaretMi.exe (
    echo ========================================
    echo   BASARILI! EXE olusturuldu:
    echo   dist\DogrulukMuCesaretMi.exe
    echo ========================================
    start dist
) ELSE (
    echo HATA: EXE olusturulamadi.
)
pause
