import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'princetonemo_project.settings')
import django
from emo.models import Department
from os import listdir
from os.path import isfile, join
import indicoio
import skimage.io
import os
from indicoio import fer, batch_fer, image_features
import django
from emo.models import UserProfile


indicoio.config.api_key = "5daca1bb2437922364bfae1c7d733109"
django.setup()


def populate():
	list_of_depts = ['Anthropology', 'Architecture', 'Art and Archaeology', 'Astrophysical Sciences', 'Chemical and Biological Engineering', 'Chemistry', 'Civil and Environmental Engineering', 'Classics', 'Comparative Literature', 'Computer Science', 'East Asian Studies', 'Ecology and Evolutionary Biology', 'Economics', 'Electrical Engineering', 'English', 'French and Italian', 'Geosciences', 'German', 'History', 'Mathematics', 'Mechanical and Aerospace Engineering', 'Molecular Biology', 'Music', 'Near Eastern Studies', 'Operations Research and Financial Engineering', 'Philosophy', 'Physics', 'Politics', 'Psychology', 'Religion', 'Slavic Languages and Literatures', 'Sociology', 'Spanish and Potuguese', 'Woodrow Wilson School of Public and International Affairs'];
	list_of_acronyms = ['ANT', 'ARC', 'ART', 'AST', 'CBE', 'CHM', 'CEE', 'CLA', 'COM', 'COS', 'EAS', 'EEB', 'ECO', 'ELE', 'ENG', 'FRE', 'GEO', 'GER', 'HIS', 'MAT', 'MAE', 'MOL', 'MUS', 'NES', 'ORF', 'PHI', 'PHY', 'POL', 'PSY', 'REL', 'SLA', 'SOC', 'SPA', 'WWS'];
	list_of_nums = [34, 26, 30, 16, 135, 72, 78, 25, 39, 324, 24, 108, 235, 104, 98, 11, 27, 11, 174, 69, 141, 121, 18, 22, 199, 53, 46, 143, 147, 27, 7, 65, 8, 315];
	for i in range(0, len(list_of_depts)):
		n = list_of_depts[i];
		a = list_of_acronyms[i];
		s = list_of_nums[i];
		department = add_dept(n, a, s);

def add_dept(name, abbr, num_students):
	d = Department.objects.get_or_create(name=name, abbr=abbr, num_students=num_students);
	return d;

def score():
	#all departments
	list_of_acronyms = ['ANT', 'ARC', 'ART', 'AST', 'CBE', 'CHM', 'CEE', 'CLA', 'COM', 'COS', 'EAS', 'EEB', 'ECO', 'ELE', 'ENG', 'FRE', 'GEO', 'GER', 'HIS', 'MAT', 'MAE', 'MOL', 'MUS', 'NES', 'ORF', 'PHI', 'PHY', 'POL', 'PSY', 'REL', 'SLA', 'SOC', 'SPA', 'WWS'];
	#list_of_acronyms = ['ANT', 'ARC', 'ART', 'AST', 'CBE', 'CHM', 'CEE'];
	#list_of_acronyms = ['CLA', 'COM', 'COS', 'EAS', 'EEB', 'ECO', 'ELE', 'ENG', 'FRE', 'GEO', 'GER'];
	#list_of_acronyms = ['HIS', 'MAT', 'MAE', 'MOL', 'MUS', 'NES', 'ORF', 'PHI'];
	#list_of_acronyms = ['PHY', 'POL', 'PSY', 'REL', 'SLA', 'SOC', 'SPA', 'WWS'];
	#go through all folders of departments
	for department in list_of_acronyms:
		directory = "/Users/Valerie/Documents/HackPrinceton/" + department;
		#get all files in that folder
		photos = [ f for f in listdir(directory) if isfile(join(directory,f)) ];
		#go through all the files
		count = 0;
		for photo in photos:
			count += 1;
			print count;
			path = directory + "/" + photo;
			pixel_array = skimage.io.imread(path).tolist()
			# print(fer(pixel_array))
			scores = fer(pixel_array)
			# start_index = scores.find(':');
			# number = "";
			# vals = [];
			# while start_index != -1:
			# 	start_index += 2;
			# 	for i in range(start_index, len(scores)):
			# 		digit = scores[i];
			# 		if not digit.isdigit():
			# 			break;
			# 		number += digit;
			# 	vals.append(int(number));
			# 	scores = scores[end_index:];
			# 	start_index = scores.find(':');

			# angry = vals[0];
			# sad = vals[1];
			# neutral = vals[2]
			# surprise = vals[3];
			# fear = vals[4];
			# happy = vals[5];

			angry = scores[u'Angry'];
			sad = scores[u'Sad'];
			neutral = scores[u'Neutral'];
			surprise = scores[u'Surprise'];
			fear = scores[u'Fear'];
			happy = scores[u'Happy'];

			dep = Department.objects.filter(abbr=department)[0]
			u = add_user(count, angry, sad, neutral, surprise, fear, happy, angry, sad, neutral, surprise, fear, happy, dep);
			old_angry_avg = dep.angry_avg;
			new_angry_avg = (old_angry_avg * (count - 1) + angry)/count;
			dep.angry_avg = new_angry_avg;

			old_sad_avg = dep.sad_avg;
			new_sad_avg = (old_sad_avg * (count - 1) + sad)/count;
			dep.sad_avg = new_sad_avg;

			old_neutral_avg = dep.neutral_avg;
			new_neutral_avg = (old_neutral_avg * (count - 1) + neutral)/count;
			dep.neutral_avg = new_neutral_avg;

			old_surprise_avg = dep.surprise_avg;
			new_surprise_avg = (old_surprise_avg * (count - 1) + surprise)/count;
			dep.surprise_avg = new_surprise_avg;

			old_fear_avg = dep.fear_avg;
			new_fear_avg = (old_fear_avg * (count - 1) + fear)/count;
			dep.fear_avg = new_fear_avg;

			old_happy_avg = dep.happy_avg;
			new_happy_avg = (old_happy_avg * (count - 1) + happy)/count;
			dep.happy_avg = new_happy_avg;
			dep.save();
			print department;


def add_user(num_scanned, angry_new, sad_new, neutral_new, surprise_new, fear_new, happy_new, angry_avg, sad_avg, neutral_avg, surprise_avg, fear_avg, happy_avg, department):
	u = UserProfile.objects.get_or_create(num_scanned=num_scanned, angry_new=angry_new, sad_new=sad_new, neutral_new=neutral_new, surprise_new=surprise_new, fear_new=fear_new, happy_new=happy_new, angry_avg=angry_avg, sad_avg=sad_avg, neutral_avg=neutral_avg, surprise_avg=surprise_avg, fear_avg=fear_avg, happy_avg=happy_avg, department=department);
	return u;

if __name__ == '__main__':
    print "Starting population script..."
    populate();
    score();