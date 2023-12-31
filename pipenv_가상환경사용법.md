pipenv는 파이썬 가상환경과 패키지 관리를 통합한 도구로, 파이썬 프로젝트를 보다 효율적으로 관리할 수 있게 도와줍니다. 아래 단계를 따라 pipenv를 사용하는 방법을 안내해 드리겠습니다.

1. pipenv 설치하기:
   파이썬 3 버전 이상이 설치되어 있는지 확인한 후, 터미널 또는 명령 프롬프트에서 다음 명령을 실행하여 pipenv를 설치합니다:
   ```
   $ pip install --user pipenv
   ```

2. 프로젝트 폴더로 이동하기:
   pipenv를 사용할 프로젝트의 폴더로 이동합니다. 예를 들어, 다음과 같은 명령을 실행하여 새로운 폴더를 생성하고 해당 폴더로 이동할 수 있습니다:
   ```
   $ mkdir myproject
   $ cd myproject
   ```

3. 가상환경 생성하기:
   다음 명령을 실행하여 가상환경을 생성합니다:
   ```
   $ pipenv shell
   ```

4. 패키지 설치하기:
   pipenv는 Pipfile이라는 파일을 사용하여 패키지 종속성을 관리합니다. 다음 명령을 실행하여 필요한 패키지를 설치합니다:
   ```
   $ pipenv install 패키지이름
   ```

5. 가상환경에서 실행하기:
   필요한 패키지를 설치한 후에는 가상환경에서 프로그램을 실행할 수 있습니다. 다음과 같이 python 명령을 사용하여 실행합니다:
   ```
   $ pipenv run python 파일이름.py
   ```

6. 종속성 관리하기:
   추가로 필요한 패키지를 설치하려면, 다음과 같이 패키지 이름을 지정하여 패키지를 설치합니다:
   ```
   $ pipenv install 추가_패키지이름
   ```

   만약 설치된 패키지 중 하나를 제거하려면, 다음과 같이 패키지 이름을 지정하여 패키지를 제거합니다:
   ```
   $ pipenv uninstall 패키지이름
   ```

   이러한 작업은 자동으로 Pipfile에 반영됩니다.

이제 pipenv를 사용하여 파이썬 프로젝트를 시작할 수 있습니다. 필요한 패키지를 관리하고 가상환경에서 프로그램을 실행하는 것이 더 편리하고 격리된 환경에서 작업할 수 있습니다.


<br>
<br>
<br>
<br>
<br>


## pipenv을 설치도중 이런문장이 뜬다면

```
WARNING: The script virtualenv.exe is installed in 'C:\Users\USER\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

해당 경고 메시지는 `virtualenv.exe` 스크립트가 PATH에 포함되어 있지 않다는 것을 알려주는 것입니다. `pipenv`는 내부적으로 `virtualenv`를 사용하므로 이 경고가 발생합니다.

이러한 경고를 해결하기 위해서는 다음 두 가지 방법 중 하나를 선택할 수 있습니다:

1. PATH에 디렉토리 추가하기:
   경고에서 제안한 대로 해당 디렉토리를 PATH 환경 변수에 추가합니다. 이렇게 하면 시스템이 `virtualenv.exe`를 찾을 수 있게 됩니다.

   - Windows에서는 다음 단계를 따릅니다:
     1. 시작 메뉴에서 "시스템 환경 변수 편집"을 검색하여 "시스템 환경 변수 편집" 창을 엽니다.
     2. "환경 변수" 버튼을 클릭합니다.
     3. "시스템 변수" 섹션에서 "Path" 변수를 선택하고 "편집" 버튼을 클릭합니다.
     4. "새로 추가" 버튼을 클릭하여 `C:\Users\USER\AppData\Roaming\Python\Python311\Scripts` 경로를 추가합니다. 여기서 `USER`는 사용자 이름에 해당하는 부분입니다.
     5. 변경된 환경 변수를 저장하고 종료합니다.

   이제 `virtualenv.exe` 스크립트가 PATH에 포함되어 있으므로 경고 메시지가 더 이상 표시되지 않을 것입니다.


 가상환경 재생성하기:
   가상환경을 생성하는 과정에서 문제가 발생했을 수 있습니다. 프로젝트 폴더에서 다음 명령을 실행하여 가상환경을 다시 생성해 보세요:
   ```
   $ pipenv --python 3.x.x   # 원하는 파이썬 버전으로 변경
   $ pipenv shell
   ```

위의 단계를 확인하고 문제가 해결되었는지 확인해 보시기 바랍니다. 만약 문제가 지속된다면, 추가적인 정보를 제공하여 더 자세한 도움을 드릴 수 있습니다.


