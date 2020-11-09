    # dist          

    python -m pep517.build .


    # published to: test.pypi.org
    # fazus
      https://packaging.python.org/guides/using-testpypi/

      pip install twine

      optionally configure $HOME/.pyprc  
		[testpypi]
	          username = [username]o

      twine upload --repository testpypi dist/*

     # download from test.pypi.org   
     pip install -i https://test.pypi.org/simple/ orange
     pip install -i https://test.pypi.org/simple/ orange --upgrade
 



