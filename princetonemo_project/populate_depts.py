import os
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

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'princetonemo_project.settings')

django.setup()


def populate():
	list_of_depts = ['Anthropology', 'Architecture', 'Art and Archaeology', 'Astrophysical Sciences', 'Chemical and Biological Engineering', 'Chemistry', 'Civil and Environmental Engineering', 'Classics', 'Comparative Literature', 'Computer Science', 'East Asian Studies', 'Ecology and Evolutionary Biology', 'Economics', 'Electrical Engineering', 'English', 'French and Italian', 'Geosciences', 'German', 'History', 'Mathematics', 'Mechanical and Aerospace Engineering', 'Molecular Biology', 'Music', 'Near Eastern Studies', 'Operations Research and Financial Engineering', 'Philosophy', 'Physics', 'Politics', 'Psychology', 'Religion', 'Slavic Languages and Literatures', 'Sociology', 'Woodrow Wilson School of Public and International Affairs'];
	list_of_acronyms = ['ANT', 'ARC', 'ART', 'AST', 'CBE', 'CHM', 'CEE', 'CLA', 'COM', 'COS', 'EAS', 'EEB', 'ECO', 'ELE', 'ENG', 'FRE', 'GEO', 'GER', 'HIS', 'MAT', 'MAE', 'MOL', 'MUS', 'NES', 'ORF', 'PHI', 'PHY', 'POL', 'PSY', 'REL', 'SLA', 'SOC', 'SPA', 'WWS'];
	list_of_nums = [34, 26, 30, 16, 135, 72, 78, 25, 39, 324, 24, 108, 235, 104, 98, 11, 27, 11, 174, 69, 141, 121, 18, 22, 199, 53, 46, 143, 147, 27, 7, 65, 8, 315];
	for i in range(0, len(list_of_depts)):
		n = list_of_depts[i];
		a = list_of_acronyms[i];
		s = list_of_nums[i];
		department = add_dept(n, a);

def add_dept(name, abbr, num_students):
	d = Department.objects.get_or_create(name=name, abbr=abbr, num_students=num_students);
	return d;

def score():
	list_of_acronyms = ['ANT', 'ARC', 'ART', 'AST', 'CBE', 'CHM', 'CEE', 'CLA', 'COM', 'COS', 'EAS', 'EEB', 'ECO', 'ELE', 'ENG', 'FRE', 'GEO', 'GER', 'HIS', 'MAT', 'MAE', 'MOL', 'MUS', 'NES', 'ORF', 'PHI', 'PHY', 'POL', 'PSY', 'REL', 'SLA', 'SOC', 'SPA', 'WWS'];
	dept_scores = [];
	for department in list_of_acronyms:
		directory = "/Users/Valerie/Documents/HackPrinceton/" + department;
		photos = [ f for f in listdir(directory) if isfile(join(directory,f)) ];
		this_dept_scores = [];
		for photo in photos:
			path = directory + "/" + photo;
			pixel_array = skimage.io.imread(path).tolist()
			this_dept_scores.append(fer(pixel_array));
		dept_scores.append(this_dept_scores);

def add_user(num_scanned, angry_new, sad_new, neutral_new, surprise_new, fear_new, happy_new, angry_avg, sad_avg, neutral_avg, surprise_avg, fear_avg, happy_avg):
	u = UserProfile.objects.get_or_create(num_scanned=num_scanned, angry_new=angry_new, angry_new=angry_new, sad_new=sad_new, neutral_new=neutral_new, surprise_new=surprise_new, fear_new=fear_new, happy_new=happy_new, angry_avg=angry_avg, sad_avg=sad_avg, neutral_avg=neutral_avg, surprise_avg=surprise_avg, fear_avg=fear_avg, happy_avg=happy_avg);
	return u;

if __name__ == '__main__':
    print "Starting population script..."
    populate();
    score();