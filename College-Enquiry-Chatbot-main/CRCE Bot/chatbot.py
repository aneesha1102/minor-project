from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

spacy.load('en_core_web_sm')


# Creating ChatBot Instance
chatbot = ChatBot('<b>CVRCE BOT</b>')


chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to  CVRCE! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///annu.sqlite3'
)
trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans
conversation = [
    "Hi",
    "Helloo!",
    "Hey",

    "How are you?",
    "I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

    "Great",
    "Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

    "good",
    "Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

    "fine",
    "Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

    "Thank You",
    "Your Welcome 😄",

    "Thanks",
    "Your Welcome 😄",

    "Bye",
    "Thank You for visiting!..",

    "What do you do?",
    "I am made to give Information about CVR college.",

    "What else can you do?",
    "I can help you know more about CVR",

    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Administrative<br>1.3 Examination <br>1.4 Placements </b>",

    "1.1",
    "<b>  CURRICULARS <br>  These are the top results: <br> <br> 1.1.1 Courses Offered <br> 1.1.2 Academic Calendar <br> 1.1.3 Course Outcomes </b>",
    "1.1.1",
    "<b> 1.1.1 Courses Offered<br>The link to Courses Offered 👉 <a href=" 'https://cvr.ac.in/home4/index.php/courses-offered' " target="'_blank'">Click Here</a> </b>",
    "1.1.2",
    "<b > 1.1.2 Academic Calender<br>The link to Academic Calender👉<a href=" 'https://cvr.ac.in/home4/index.php/academic-calendars' " target="'_blank'">Click Here</a> </b>",
    "1.1.3",
    "<b> 1.1.3 Course Outcomes<br>The link to Syllabus 👉 <a href=" 'https://cvr.ac.in/home4/index.php/academics/course-outcomes' " target="'_blank'">Click Here</a> </b>",


    "1.2",
    "<b>1.2 ADMINISTRATIVE<br>These are the top results: <br> <br> 1.2.1 Student center <br> 1.2.2 Notifications </b>",
    "1.2.1",
    "<b> 1.2.1 Student center <br>The link to Students Portal👉 <a href=" 'https://cvr.ac.in/home4/index.php/student-center' ">Click Here</a> </b>",
    "1.2.2",
    "<b> 1.2.2 Notifications <br>The link to Notices👉 <a href=" 'https://drive.google.com/drive/folders/1VN7P2befLz46hDcEZPcg0C16JwyX0H6s' ">Click Here</a> </b>",

    "1.3",
    "<b > EXAMINATION <br>These are the top results:<br> 1.3.1 Examination branch <br> <br>",
    "1.3.1",
    "<b > 1.3.1 Examination branch <br>The link to Notices👉 <a href=" 'https://cvr.ac.in/home4/index.php/examination-branch' ">Click Here</a> </b>",


    "1.4",
    "<b > PLACEMENTS These are the top results:<br> 1.4.1 Placements Records<br> 1.4.2 Our Recruiters <br> 1.4.3 Placement Statistics 2022</b>",
    "1.4.1",
    "<b> 1.4.1 Placements Records<br>The link to Placements Records👉 <a href=" 'https://cvr.ac.in/home4/index.php/placements' ">Click Here</a> </b>",
    "1.4.2",
    "<b> 1.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://cvr.ac.in/home4/index.php/placements' ">Click Here</a> </b>",
    "1.4.3",
    "<b > 1.4.3 Placement Statistics<br>The link to Placement Statistics 2022👉 <a href=" 'https://cvr.ac.in/home4/index.php/placements' ">Click Here</a> </b>",

    "2",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Faculty details <br>2.2  Examination </b>",

    "2.1",
    "<b > FACULTY DETAILS These are the top results:<br>2.1.1 Civil </b>",

    "2.1.1",
    "<b> 2.1.1 Civil <br>The link to Moodle👉<a href=" 'https://cvr.ac.in/home4/index.php/civil/civilfaculty' ">Click Here</a> </b>",


    "2.2",
    "<b > EXAMINATION <br>These are the top results:<br> <br> 2.2.1 Notifications <br> ",
    "2.2.1",
    "<b> 2.2.1 Notifications <br>The link to Notices 👉 <a href=" 'https://drive.google.com/drive/folders/1VN7P2befLz46hDcEZPcg0C16JwyX0H6s' ">Click Here</a> </b>",

    "3",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Notices <br>3.3 Fee Payment <br>3.4 Placements </b> ",

    "3.1",
    "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About CVRCE<br> 3.1.2 College Address <br> 3.1.3 Hostel Facility <br> 3.1.4 Transport Facility </b>",
    "3.1.1",
    "<b > 3.1.1 About CVRCE<br>The link to About CVRCE👉 <a href=" 'https://cvr.ac.in/home4/index.php/chairman-message' ">Click Here</a> </b>",
    "3.1.2",
    "<b > 3.1.2 College Address <br>address:-Mangalpally x road,Ibrahimpatnam,Hyderabad, Telangana 501510.The link to college Address👉<a href=" 'https://cvr.ac.in/home4/index.php/address' ">Click Here</a> </b>",
    "3.1.3",
    "<b > 3.1.3 Hostel facility <br>The link to Hostel Facility👉 <a href=" 'https://cvr.ac.in/home4/index.php/hostel' ">Click Here</a> </b>",
    "3.1.4",
    "<b > 3.1.4 Transport facility <br>The link to Transport Facility👉 <a href=" 'https://cvr.ac.in/home4/index.php/buses' ">Click Here</a> </b>",
    "3.2",
    "<b > NOTICES<br>These are the top results:<br> <br> 3.2.1 All Notifications  </b>",
    "3.2.1",
    "<b > 3.2.1 All Notifications <br>The link to All Notices👉 <a href=" 'https://drive.google.com/drive/folders/1VN7P2befLz46hDcEZPcg0C16JwyX0H6s' ">Click Here</a> </b>",

    "3.3",
    "<b >FEE PAYMEMT<br>These are the top results:<br> <br>3.3.1 Payment Portal <br>  </b>",
    "3.3.1",
    "<b > 3.3.1 Payment Details<br>The link to Payment Portal 👉 <a href=" 'https://www.onlinesbi.sbi/sbicollect/icollecthome.htm?corpID=958125' ">Click Here</a> </b>",

    "3.4",
    "<b > PLACEMENTS These are the top results:<br> <br>3.4.1 Placements<br> 3.4.2 Our Recruiters <br> 3.4.3 Placement Statistics </b>",
    "3.4.1",
    "<b> 3.4.1 Placements<br>The link to Placement records👉 <a href=" 'https://cvr.ac.in/home4/index.php/placements' ">Click Here</a> </b>",
    "3.4.2",
    "<b> 3.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://cvr.ac.in/home4/index.php/placements' ">Click Here</a> </b>",
    "3.4.3",
    "<b > 3.4.3 Placement Statistics<br>The link to Placement Statistics 2022👉 <a href=" 'https://cvr.ac.in/home4/index.php/placements' ">Click Here</a> </b>",

    "4",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 About Us<br></b>",

    "4.1",
    "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 About CVRCE<br> 4.1.2 College Address <br> 4.1.3 Hostel Facility <br> 4.1.4 Transport Facility </b>",
    "4.1.1",
    "<b > 4.1.1 About CVRCE<br>The link to About CVRCE👉 <a href=" 'https://cvr.ac.in/home4/index.php/chairman-message' ">Click Here</a> </b>",
    "4.1.2",
    "<b > 4.1.2 College Address <br>address:-Mangalpally x road,Ibrahimpatnam,Hyderabad, Telangana 501510.The link to college Address👉<a href=" 'https://cvr.ac.in/home4/index.php/address' ">Click Here</a> </b>",
    "4.1.3",
    "<b > 4.1.3 Hostel facility <br>The link to Hostel Facility👉 <a href=" 'https://cvr.ac.in/home4/index.php/hostel' ">Click Here</a> </b>",
    "4.1.4",
    "<b > 4.1.4 Transport facility <br>The link to Transport Facility👉 <a href=" 'https://cvr.ac.in/home4/index.php/buses' ">Click Here</a> </b>",


]

trainer.train(conversation)
