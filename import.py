#!/usr/bin/python
import json
import os
import errno
import sys
import codecs
from datetime import date
from datetime import datetime
from pprint import pprint
from string import Template

def read(input_file):
	json_file = codecs.open(input_file, 'r', 'utf-8')
	data = json.load(json_file)
	json_file.close()
	return data

def is_published(post):
	if status(post) == "published":
		return post
	else:
		return None

def is_draft(post):
	if not is_published(post):
		return post
	else:
		return None

def title(post):
	return post["title"]

def markdown(post):
	return post["markdown"]

def slug(post):
	return post["slug"]

def status(post):
	return post["status"]

def created(post):
	return post["created_at"]

def published(post):
	return post["published_at"]

def uuid(post):
	return post["uuid"]

def tags_for_post(post, tags, posts_tags):
	"""Returns the list of tags for the given post."""
	list_of_tags = []
	post_tags = filter(lambda p: p["post_id"] == post["id"], posts_tags)
	for post_tag in post_tags:
		# get tag
		tag_id = post_tag["tag_id"]
		tag = filter(lambda tag: tag["id"] == tag_id, tags)[0]
		#add to tag list
		list_of_tags.append(tag["slug"])
	return list_of_tags

def write(prefix, post):
	"""Writes the given post to a file."""
	# add tags to post
	post['tags'] = "\n -".join(tags_for_post(post, tags, posts_tags))
	
	if post["published_at"]:
	    d = datetime.strptime(post["published_at"], '%Y-%m-%d %H:%M:%S')
		#d = date.fromtimestamp(post["published_at"]/1000)
	else:
		d = date.today()
	slug = post["slug"]
	post["isodate"] = d.strftime('%Y-%m-%d %H:%M:%S %z')
	fpost = codecs.open(prefix + d.strftime('%Y-%m-%d') + '-' + slug + '.md', 'w', 'utf-8')
	fpost.write(s.substitute(post))
	fpost.close()

def make_sure_path_exists(path):
  try:
    os.makedirs(path)
  except OSError as exception:
    if exception.errno != errno.EEXIST:
      raise

input_file = sys.argv[1]
print "Reading data from " + input_file
data = read(input_file)

# get needed data
posts = data["db"][0]["data"]["posts"]
tags = data["db"][0]["data"]["tags"]
posts_tags = data["db"][0]["data"]["posts_tags"]

# split into published/draft
published = filter(lambda p: p != None, map(is_published, posts))
drafts = filter(lambda p: p != None, map(is_draft, posts))

### create files
s = Template("""---
layout: post
title: '$title'
main-class: 'dev'
date: $isodate
description: derscricao
color: '#637a91'
tags: $tags
layout: post
introduction: introducao
---

$markdown
""")

print "Published: " + str(len(published)) + " Draft: " + str(len(drafts))

# loop over published, create _posts/YYYY-MM-DD-'slug'.markdown
folder_posts = '_posts/'
make_sure_path_exists(folder_posts)
for post in published:
	write(folder_posts, post)

# loop over drafts, create _drafts/YYYY-MM-DD-'slug'.markdown
folder_drafts = '_drafts/'
make_sure_path_exists(folder_drafts)
for post in drafts:
	write(folder_drafts, post)

