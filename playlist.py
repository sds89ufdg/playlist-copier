#!/usr/local/bin/python3

import os, shutil, argparse, subprocess

files = []

def process_cmdline():
	parser = argparse.ArgumentParser(description='Swinsian Playlist - file copier')
		
	parser.add_argument('-p', '--playlist', help='playlist to load',required=True)
	parser.add_argument('-o', '--destination', help='directory to copy files to',required=True)
	
	args = parser.parse_args()
	
	global playlist, destination
	
	playlist = args.playlist
	destination = args.destination+os.path.basename(playlist).split(".")[0]+"/"


def os_command_output(command_run):
	command_execute = subprocess.Popen(command_run, stdout=subprocess.PIPE, shell=True)
	(command_execute_output, err) = command_execute.communicate()
	command_execute_status = command_execute.wait()

	return command_execute_output

def create_file_array():
	if os.path.isfile(playlist):
		f = open(playlist, encoding="utf-8").read().splitlines()

		for line in iter(f):
			if not line.startswith("#"):
				fullfile = "\"/"+line.strip("../")+"\""
							
				try:
					os.path.isfile(fullfile)

					OS_AUDIO_INFO = "mediainfo --Language=raw \"--output=Audio;%Format%|%BitDepth/String%|%Format/Info%\" "+ fullfile
					OS_AUDIO_INFO2 = "mediainfo --Language=raw \"--output=General;%Performer%|%Album%|%Track/Position%|%Track%\" "+ fullfile

					FILE_INFO=os_command_output(OS_AUDIO_INFO).decode('utf-8')
					FILE_INFO2=os_command_output(OS_AUDIO_INFO2).decode('utf-8')
					FILE_DETAILS=FILE_INFO.rstrip()+"|"+FILE_INFO2.rstrip()+"|"+fullfile
					
					files.append(FILE_DETAILS)

					
				except IOError as e:    
					print (e, ":audio file does not exist")
				
			
	else:
		print ("FATAL: "+playlist+" does not exist")

def process_files():

	for entry in files:

		delete_src_flac = "n"

		codec, rate, type_full, artist, album, track_num, track_name, filefull = entry.split('|')
		filename = os.path.basename(filefull).strip("\"")

		dest_dir = os.path.join(destination, artist, album)

		
		file2=filefull.strip("\"")

		if codec == 'ALAC':
			filefull = convert_alac_to_flac(filefull,filename)
			delete_src_flac = "y"
		
		if os.path.exists(file2):
			os.makedirs(dest_dir, exist_ok=True)

			OS_COPY = "cp -v "+filefull+" \""+dest_dir+"\""
			os.system(OS_COPY)

			if delete_src_flac == 'y':
				OS_REMOVE_FILE = "rm -f " + filefull
				os.system(OS_REMOVE_FILE)


			

def convert_alac_to_flac(filefull,filename):
	name, file_extension = os.path.splitext(filename)
	filefull_org = filefull
	filefull = "\"/tmp/"+ name + ".flac\""

	OS_AUDIO_CONVERT = "ffmpeg -v error -i " + filefull_org + " -c: flac " + filefull + " -y"
	os.system(OS_AUDIO_CONVERT)

	return filefull



process_cmdline()
create_file_array()
process_files()






