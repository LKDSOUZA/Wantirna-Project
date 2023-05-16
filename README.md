# Wantirna-Project

"Flask application for making predictions for house prices and ability to afford a house"

- Create a new conda environment for this app with the following code:

- All of the project dependencies will be installed in this environment.

- Note: This should contain only python 3.7—and not anaconda.

```bash
conda create -n wantirna_env python=3.7
```

- Activate this new environment before proceeding.

```bash
conda activate wantirna_env

# Note: If you run into issues, try the following command instead.
source activate wantirna_env
```

- Install the libraries into your new environment.

```bash
# install pip packages listed in requirements file 
pip install -r requirements.txt
```

- Next, to make the run.sh file executable, run the following command:

```bash
chmod a+x run.sh
```

Test the application by running the following in your command line.

```bash
./run.sh
```

- Navigate to 127.0.0.1:5000 to view the webpage and test out the app locally.

- This starter code uses a .sqlite file as the database.
