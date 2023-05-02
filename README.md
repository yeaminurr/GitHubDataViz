# The GitHub Data Viz

This is a Django-based GitHub Data Visualization tool. Which helps the user to track information like issue importance, important users, comments, etc.

##### Currently, the application supports four popular GitHub repositories: 
- Matomo
- React-native
- Haystack
- Deepchem

To make the project simple for now for every repository a new Django application has been made.

##### Here are the different repository names and their corresponding project names

- Deepchem -> firstapp
- Matomo -> matomo
- Haystack -> haystack
- React-native -> react

#### The Backend processes and logic are controlled by the project name/views.py file. Vews.py file contains - 

- Processes are those that are needed to load the application every time (Method - githubproject).
- Different APIs

##### APIs :
- **{Repository Name}/pullclick :** This API is responsible for showing the list of pull requests on a particular date. When a user clicks on the circles of the "file changed" this API is triggered and returns the result as CSV into the static folder.
- **{Repository Name}/githubproject :** This method also use as an API when any post request is sent. It is responsible for showing the list of issues on a particular date. When a user clicks on the circles of the "issue solved" this API is triggered and returns the result as CSV into the static folder.
- **{Repository Name}/labelsort :** When any label is selected from the taglist or date dropdown menu this API is called and it sends a post request with all the selected data from the dropdown, and this API process and sorts all the data according to the user selection and returns the result as CSV into the static folder.
- **{Repository Name}/commentcat :**  This API is only for fetching the user list who commented on a particular time(after clicking on the bar chart).
- **{Repository Name}/userinfo/{username} :**  This API returns information of any users in the repository in JSON format. This API is triggered when users click on the nodes of the "Collaboration Network of the contributors" chart.
- **{Repository Name}/normalize/ :**  This API returns the normalized version of the "Monthly activity of Issues and Pull requests"








