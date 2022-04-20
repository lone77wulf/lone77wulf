####################
# Author: Ted Langdon
# Date: 4/20/2022
# Notes: 
####################

#import pandas library

import pandas as pd

#open raw data file from tweet collector

pull = pd.read_csv('a.csv')

#filter our @ username mentions
#in a real environment this would be a filter IN for the agency username

noAt = pull.loc[(pull['text'].str.startswith("@")==False)]

#filter out retweets

noRT = noAt.loc[(pull['text'].str.startswith("RT")==False)]

#filter out duplicates

dedup = noRT.drop_duplicates(subset=['text'])

#create a list of the tweets matching breathing words

breathe_keyword = dedup.loc[(dedup['text'].str.contains("heart"))|
(dedup['text'].str.contains("breath")) | 
(dedup['text'].str.contains("breathe")) | 
(dedup['text'].str.contains("breathing")) | 
(dedup['text'].str.contains("breathed")) |
(dedup['text'].str.contains("asthma"))|
(dedup['text'].str.contains("pulmon"))|
(dedup['text'].str.contains("breathed"))|
(dedup['text'].str.contains("pneumonia"))|
(dedup['text'].str.contains("respir"))|
(dedup['text'].str.contains("trach")) ]

#create a filtered list from keyword list for breathing

breathe_filtered = breathe_keyword.loc[
(breathe_keyword['text'].str.contains("airway"))| 
(breathe_keyword['text'].str.contains("altered")) | 
(breathe_keyword['text'].str.contains("apnea")) | 
(breathe_keyword['text'].str.contains("aspirate")) | 
(breathe_keyword['text'].str.contains("bronchitis"))|
(breathe_keyword['text'].str.contains("canula"))| 
(breathe_keyword['text'].str.contains("choke")) | 
(breathe_keyword['text'].str.contains("COPD")) |
(breathe_keyword['text'].str.contains("covid")) | 
(breathe_keyword['text'].str.contains("corona"))| 
(breathe_keyword['text'].str.contains("cpap")) | 
(breathe_keyword['text'].str.contains("dioxide")) | 
(breathe_keyword['text'].str.contains("emphysema")) | 
(breathe_keyword['text'].str.contains("fenta"))| 
(breathe_keyword['text'].str.contains("gag")) | 
(breathe_keyword['text'].str.contains("gasp")) | 
(breathe_keyword['text'].str.contains("heavy")) | 
(breathe_keyword['text'].str.contains("hypervent"))| 
(breathe_keyword['text'].str.contains("hypox")) | 
(breathe_keyword['text'].str.contains("lodge")) | 
(breathe_keyword['text'].str.contains("monoxide")) | 
(breathe_keyword['text'].str.contains("shellfish"))|
(breathe_keyword['text'].str.contains("short"))| 
(breathe_keyword['text'].str.contains("snore")) | 
(breathe_keyword['text'].str.contains("wheeze")) |
(breathe_keyword['text'].str.contains("albuterol")) | 
(breathe_keyword['text'].str.contains("attack"))|
(breathe_keyword['text'].str.contains("inhaler"))| 
(breathe_keyword['text'].str.contains("embolism")) | 
(breathe_keyword['text'].str.contains("issue")) |
(breathe_keyword['text'].str.contains("problem")) |
(breathe_keyword['text'].str.contains("mushroom"))]

#write the filtered data to a csv to then be converted to EIDO later

breathe_filtered.to_csv('breathe_filtered.csv')

#create a list of the tweets matching fall words

fall_keyword = dedup.loc[(dedup['text'].str.contains("fall"))| 
(dedup['text'].str.contains("fell")) | 
(dedup['text'].str.contains("falling")) | 
(dedup['text'].str.contains("falls")) |
(dedup['text'].str.contains("trip"))| 
(dedup['text'].str.contains("tripped")) | 
(dedup['text'].str.contains("trips")) |
(dedup['text'].str.contains("tripping")) | 
(dedup['text'].str.contains("slip"))| 
(dedup['text'].str.contains("slipped")) | 
(dedup['text'].str.contains("slips")) | 
(dedup['text'].str.contains("slipping"))]

#create a filtered list from keyword list falls

fall_filtered = fall_keyword.loc[
(fall_keyword['text'].str.contains("ankle"))| 
(fall_keyword['text'].str.contains("arm")) | 
(fall_keyword['text'].str.contains("belly")) | 
(fall_keyword['text'].str.contains("body")) | 
(fall_keyword['text'].str.contains("bone"))|
(fall_keyword['text'].str.contains("cheek"))| 
(fall_keyword['text'].str.contains("ears")) | 
(fall_keyword['text'].str.contains("elbow")) |
(fall_keyword['text'].str.contains("eye")) | 
(fall_keyword['text'].str.contains("face"))| 
(fall_keyword['text'].str.contains("feet")) | 
(fall_keyword['text'].str.contains("femur")) | 
(fall_keyword['text'].str.contains("finger")) | 
(fall_keyword['text'].str.contains("foot"))| 
(fall_keyword['text'].str.contains("forehead")) | 
(fall_keyword['text'].str.contains("groin")) | 
(fall_keyword['text'].str.contains("hand")) | 
(fall_keyword['text'].str.contains("head"))| 
(fall_keyword['text'].str.contains("hip")) | 
(fall_keyword['text'].str.contains("jaw")) | 
(fall_keyword['text'].str.contains("joint")) | 
(fall_keyword['text'].str.contains("knee"))|
(fall_keyword['text'].str.contains("leg"))| 
(fall_keyword['text'].str.contains("lump")) | 
(fall_keyword['text'].str.contains("mouth")) |
(fall_keyword['text'].str.contains("neck")) | 
(fall_keyword['text'].str.contains("nose"))|
(fall_keyword['text'].str.contains("pelvis"))| 
(fall_keyword['text'].str.contains("rib")) | 
(fall_keyword['text'].str.contains("shoulder")) |
(fall_keyword['text'].str.contains("skin")) |
(fall_keyword['text'].str.contains("spine")) |
(fall_keyword['text'].str.contains("tail")) |
(fall_keyword['text'].str.contains("tooth")) |
(fall_keyword['text'].str.contains("thighs")) |
(fall_keyword['text'].str.contains("thumb"))]

#write the filtered data to a csv to then be converted to EIDO later

fall_filtered.to_csv('fall_filtered.csv')

#create a list of the tweets matching heart words

heart_keyword = dedup.loc[(dedup['text'].str.contains("heart"))|
(dedup['text'].str.contains("meds")) |
(dedup['text'].str.contains("pain")) ]

#create a filtered list from keyword list for heart conditions

heart_filtered = heart_keyword.loc[
(heart_keyword['text'].str.contains("afib"))| 
(heart_keyword['text'].str.contains("aneurism")) | 
(heart_keyword['text'].str.contains("angina")) | 
(heart_keyword['text'].str.contains("aortic")) | 
(heart_keyword['text'].str.contains("arrest"))|
(heart_keyword['text'].str.contains("attack"))| 
(heart_keyword['text'].str.contains("beating")) | 
(heart_keyword['text'].str.contains("embolism")) |
(heart_keyword['text'].str.contains("failure")) | 
(heart_keyword['text'].str.contains("fibrilation"))| 
(heart_keyword['text'].str.contains("pacemaker")) | 
(heart_keyword['text'].str.contains("racing")) | 
(heart_keyword['text'].str.contains("rapid")) | 
(heart_keyword['text'].str.contains("tachycardia"))| 
(heart_keyword['text'].str.contains("asprin")) | 
(heart_keyword['text'].str.contains("glycerin")) | 
(heart_keyword['text'].str.contains("nitro")) | 
(heart_keyword['text'].str.contains("thinners"))| 
(heart_keyword['text'].str.contains("chest")) | 
(heart_keyword['text'].str.contains("crushing")) | 
(heart_keyword['text'].str.contains("radiating")) | 
(heart_keyword['text'].str.contains("elephant"))]

#write the filtered data to a csv to then be converted to EIDO later

heart_filtered.to_csv('heart_filtered.csv')

#create a list of the tweets matching words that show in multiple types of incidents

multi_issue_keyword = dedup.loc[(dedup['text'].str.contains("heart"))| 
(dedup['text'].str.contains("breath")) | 
(dedup['text'].str.contains("breathe")) | 
(dedup['text'].str.contains("breathing")) | 
(dedup['text'].str.contains("breathed"))|
(dedup['text'].str.contains("fall"))| 
(dedup['text'].str.contains("fell")) | 
(dedup['text'].str.contains("falling")) |
(dedup['text'].str.contains("falls")) | 
(dedup['text'].str.contains("trip"))| 
(dedup['text'].str.contains("tripped")) | 
(dedup['text'].str.contains("trips")) | 
(dedup['text'].str.contains("tripping")) | 
(dedup['text'].str.contains("slip"))| 
(dedup['text'].str.contains("slipped")) | 
(dedup['text'].str.contains("slips")) | 
(dedup['text'].str.contains("slipping"))]

#create a list of the tweets matching heart words

multi_issue_filtered = multi_issue_keyword.loc[(multi_issue_keyword['text'].str.contains("blood"))| 
(multi_issue_keyword['text'].str.contains("collapse")) | 
(multi_issue_keyword['text'].str.contains("confusion")) | 
(multi_issue_keyword['text'].str.contains("conscious")) | 
(multi_issue_keyword['text'].str.contains("chronic"))|
(multi_issue_keyword['text'].str.contains("dazed"))| 
(multi_issue_keyword['text'].str.contains("disorient")) | 
(multi_issue_keyword['text'].str.contains("dizzy")) |
(multi_issue_keyword['text'].str.contains("lethar")) | 
(multi_issue_keyword['text'].str.contains("meds"))| 
(multi_issue_keyword['text'].str.contains("muscle")) | 
(multi_issue_keyword['text'].str.contains("numb")) | 
(multi_issue_keyword['text'].str.contains("slur")) | 
(multi_issue_keyword['text'].str.contains("spasms"))| 
(multi_issue_keyword['text'].str.contains("throb")) | 
(multi_issue_keyword['text'].str.contains("unsteady")) | 
(multi_issue_keyword['text'].str.contains("vital")) | 
(multi_issue_keyword['text'].str.contains("vertigo"))|
(multi_issue_keyword['text'].str.contains("blacking"))| 
(multi_issue_keyword['text'].str.contains("anxiety")) | 
(multi_issue_keyword['text'].str.contains("blur")) | 
(multi_issue_keyword['text'].str.contains("burn")) | 
(multi_issue_keyword['text'].str.contains("chronic"))|
(multi_issue_keyword['text'].str.contains("clammy"))| 
(multi_issue_keyword['text'].str.contains("congest")) | 
(multi_issue_keyword['text'].str.contains("distress")) |
(multi_issue_keyword['text'].str.contains("dose")) | 
(multi_issue_keyword['text'].str.contains("drug"))| 
(multi_issue_keyword['text'].str.contains("foaming")) | 
(multi_issue_keyword['text'].str.contains("irregular")) | 
(multi_issue_keyword['text'].str.contains("labor")) | 
(multi_issue_keyword['text'].str.contains("manic"))| 
(multi_issue_keyword['text'].str.contains("narcan")) | 
(multi_issue_keyword['text'].str.contains("obstruct")) | 
(multi_issue_keyword['text'].str.contains("onset")) | 
(multi_issue_keyword['text'].str.contains("oxyc"))|
(multi_issue_keyword['text'].str.contains("palpate")) | 
(multi_issue_keyword['text'].str.contains("panic")) | 
(multi_issue_keyword['text'].str.contains("pressure"))| 
(multi_issue_keyword['text'].str.contains("tense")) | 
(multi_issue_keyword['text'].str.contains("tingle")) | 
(multi_issue_keyword['text'].str.contains("treatment")) | 
(multi_issue_keyword['text'].str.contains("oxy"))]

#write the filtered data to a csv to then be converted to EIDO later

multi_issue_filtered.to_csv('Multi_Issue_Filtered.csv')
