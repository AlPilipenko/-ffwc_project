# ffwc_project

<h2>FFWC - Friends & Family Weight Challenge</h2>
Summer is coming! It is time to trim the fat that we gained during the winter.<br/>
This app allows members of friends and families to keep track of their weight loss progress. This is how it works: members record their initial weight and set up their goal weight which they will be trying to achieve. Everyone will be able to see the joined goal (total weight to lose) and contribute as much as they can to achieve this goal. Basically, 'well-performing' members can help those members who are struggling to lose weight to share the load and lose more weight to contribute towards the total goal.

<h2>Setup instructions (step by step):</h2>


  1. Download this repository.
  2. Unpack the contents of the zip file.
  3. Install the latest Python version if you haven't already.
  4. Run the CMD or other terminal that supports Python.
  5. In the terminal navigate to the root of the unpacked folder.
  6. Run the following commands in the terminal:
  <ul>
  <li>python -m pip install --upgrade pip</li>
  <li>python -m venv .\environments\ffwc</li>
  <li>environments\ffwc\Scripts\activate</li>
  <li>pip install Django</li>
  <li>pip install matplotlib</li>
  <li>python manage.py runserver</li>
  </ul>
  
  7. Go to your local host - 127.0.0.1:8000
  8. Play around :)
  
  I have already populated the database with two users:
  <ul>
  <li>Admin - Login: Pandora1, Password: assignment1</li>
  <li>Normal user - Login: John, Password: assignment1</li>
  </ul>
    
Feel free to create more users and add weight records (two records are  required two see changes in the plot). The users cannot delete themselves, so you have to go to the 127.0.0.1:8000/admin and log in as Admin in order to delete them.



Important! Do not install requirements with pip command! For some reason it didn't work on the 2nd machine I was testing the project on. Manual pip installation of Django and matplotlib helped to start the server. Also, if you want to you could skip the installation of the environment
