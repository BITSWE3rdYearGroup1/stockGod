# stockGod
stockGod is a school project that we are making, it uses Linear Regression as a model algorithm and [Google's Stock Price](https://www.kaggle.com/datasets/akpmpr/google-stock-price-all-time) as its Dataset.
## to run it on your machine follow this steps.
1. Install python and anacoda 
* _[Python](https://www.python.org/downloads/)_
* _[Anaconda](https://www.anaconda.com/download)_
2. Install dependencies
* create environment activate your environment
```
conda create --name yourEnvName
conda activate yourEnvName
```
* install _pandas_, _scikit-learn_, _matplotlib_, _pyqt5_ and _pickle_
```
conda install pandas
conda insta scikit-learn
pip install matplotlib
pip install pyqt5
pip install pickle
```

3. run it on your machine
> run _app.py_ file with your python interpreter


## Bundling into executable
**make sure your environment is activated**
1. install _pyinstaller_
```
pip install pyinstaller
```
2. create package folder named '_package_' move _app.py_, _StockGod.py_ and _trained_model.pkl_ into it.
 **it is not necessary but to make your repo clean and not to track that huge executable file you gonna create, you better not skip this step**
3. change your terminal directory and run the following commands
```
pyinstaller --name=G-Stock --onefile app.py
```
4. Edit the spec file only _hiddenimports_ list like the following
```
a = Analysis(['app.py'],
             hiddenimports=['sklearn', 'pickle', 'pandas', 'matplotlib', 'PyQt5'])
```
5. run this command on your current terminal
```
pyinstaller G-Stock.spec
```
after the command finish executing you will have your executable file in _/dist_ file in your _package_ folder.

*Enjoy Using It If it works, BTW it works on my machine 😜 you get it.*
