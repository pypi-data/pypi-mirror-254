import pytest
from processing import *
import numpy as np

@pytest.mark.parametrize("test_input,expected", 
                         [("We will, we will rock you We will, we will rock you Buddy, you're a young man, hard man", np.array([2, 2, 2, 2,
                                                                                                                                2, 2, 1, 1,
                                                                                                                                1, 1, 1,
                                                                                                                                1, 1]))])
def test_bar_plot_values(test_input, expected):
    bar_plot_input, bar_plot_test = bar_plot(test_input)
    assert (bar_plot_test == expected).all()
    
@pytest.mark.parametrize("test_input,expected", 
                         [("We will, we will rock you We will, we will rock you Buddy, you're a young man, hard man", ['We', 'will,', 'we',
                                                                                                                       'will','rock','you','Buddy,',"you're",'a','young','man,','hard','man'])])
def test_bar_plot_names(test_input, expected):
    bar_plot_input, bar_plot_test = bar_plot(test_input)
    assert bar_plot_input == expected

@pytest.mark.parametrize("test_input,expected", 
                         [("Don't stop me now, I'm having such a good time I'm having a ball Don't stop me now", 38)])   
def test_pie_chart_names(test_input, expected):
    assert len(pie_chart(test_input)) == expected

@pytest.mark.parametrize("test_input,expected", 
                         [("Often said when things are still not decided. Plans still need to be finalized.", [1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])])
def test_cloud_words(test_input, expected):
    cw = list(cloud_words(test_input).words_.values())
    assert cw == expected

@pytest.mark.parametrize("test_input,expected", 
                         [("Never give in. Never give in. Never, never, never, never-in nothing, great or small, large or petty-never give in, except to convictions of honor and good sense.", 7)])
def test_plot_word_frequency(test_input, expected):
    wf = len(plot_word_frequency(test_input).gca().get_yticklabels())
    assert wf == expected

@pytest.mark.parametrize("text, expected", [
    ("Hi How are you!$%&/()", "Hi How are you"),
    ("This is an example/()=?", "This is an example"),
    ("Christmas is !""#the best time of the year%&/()==)()", "Christmas is the best time of the year"),
    
])
def test_remove_characters(text, expected):
    assert remove_characters(text) == expected

@pytest.mark.parametrize("text, expected", [
    (['I','like','playing','computer','games'], [ 'like', 'playing', 'computer', 'games']),
    (['hate', 'fast', 'food', 'restaurants'], ['hate', 'fast', 'food', 'restaurants']),
    (['The','best','book','of','all','times','is','from','kafka'], ['best', 'book', 'times', 'kafka'])
    
])
def test_remove_stopwords(text, expected):
    assert remove_stopwords(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("THIS IS A TEST", "this is a test"),
    ("I LIKE READING COMICS", "i like reading comics"),
    ("THE APPLE PIE IS MY FAVOURITE", "the apple pie is my favourite")
    
])
def test_convert_to_lowercase(text, expected):
    assert convert_to_lowercase(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("🌟Just finished an amazing workout session! Feeling so energized and ready to conquer the day!💪", "Just finished an amazing workout session! Feeling so energized and ready to conquer the day!"),
    ("😞Stuck in traffic again... why does this always happen during rush hour?", "Stuck in traffic again... why does this always happen during rush hour?"),
    ("📉Disappointed with the latest company decision. Feels like a step backward instead of forward.", "Disappointed with the latest company decision. Feels like a step backward instead of forward."),
   
])
def test_remove_emojis(text, expected):
    assert remove_emojis(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Stuck in traffic  again...  why  does  this", "Stuck in traffic again... why does this"),
    ("Just  finished  an  amazing workout  session", "Just finished an amazing workout session"),
    ("There's  nothing  like a  peaceful morning", "There's nothing like a peaceful morning"),
])
def test_remove_extra_spaces(text, expected):
    assert remove_extra_spaces(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("123abc456def789", "abcdef"),
    ("Stuck in traffic again 123abc456def789", "Stuck in traffic again abcdef"),
    ("Disappointed with the latest company decision. Feels 12343", "Disappointed with the latest company decision. Feels "),
    # Add more test cases here for remove_numbers
])
def test_remove_numbers(text, expected):
    assert remove_numbers(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Just had an amazing brainstorming session with @TechInnovator21! Their innovative ideas are always inspiring. 💡🚀 #Collaboration #Innovation","Just had an amazing brainstorming session with  Their innovative ideas are always inspiring. 💡🚀 #Collaboration #Innovation"),
    ("Attended a seminar by @MarketingGuru45 today! Their insights on social media strategies were incredibly enlightening. 📱✨ #MarketingTips #LearnFromTheBest","Attended a seminar by  today! Their insights on social media strategies were incredibly enlightening. 📱✨ #MarketingTips #LearnFromTheBest"),
    ("Had a fantastic interview with @MusicMaestro88! Their passion for music truly shines through. 🎶🎤 #MusicalGenius #InterviewInsights","Had a fantastic interview with  Their passion for music truly shines through. 🎶🎤 #MusicalGenius #InterviewInsights")
])
def test_remove_users(text, expected):
    assert remove_users(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Exploring new heights 🏞️ #AdventureTime #PeakViews", "Exploring new heights 🏞️  "),
    ("Baking bliss 🥖🍰 #HomeBakerJoys #OvenMagic", "Baking bliss 🥖🍰  "),
    ("Fitness journey begins! 💪🏋️ #NewGoals #HealthyHabits","Fitness journey begins! 💪🏋️  "),

])
def test_remove_hastags(text, expected):
    assert remove_hastags(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("This is a link: https://example.com", "This is a link: "),
    ("Learn how to master coding basics in no time! 💻🚀 Link: https://codinglessons.com/basics #CodingSkills #TechEducation", "Learn how to master coding basics in no time! 💻🚀 Link:  #CodingSkills #TechEducation"),
    # Add more test cases here for remove_links
])
def test_remove_links(text, expected):
    assert remove_links(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Python programmers often tend like programming in python", "python programm often tend like program in python"),
    ("Something we have not touched on much in this tutorial","someth we have not touch on much in thi tutori"),
    ("You would need a good knowledge and understanding of the target language to build a lemmatizer","you would need a good knowledg and understand of the target languag to build a lemmat"),
    ("To summarize, stemming and lemmatization are techniques used for text processing in NLP","to summar stem and lemmat are techniqu use for text process in nlp"),
    ("The stemming approach is much faster than lemmatization","the stem approach is much faster than lemmat")
])
def test_transform_stemmer(text, expected):
    assert transform_stemmer(text) == expected

@pytest.mark.parametrize("text, expected",[
    ("Python programmers often tend like programming in python", "Python programmer often tend like programming in python"),
    ("Something we have not touched on much in this tutorial", "Something we have not touched on much in this tutorial"),
    ("You would need a good knowledge and understanding of the target language to build a lemmatizer","You would need a good knowledge and understanding of the target language to build a lemmatizer"),
    ("To summarize, stemming and lemmatization are techniques used for text processing in NLP","To summarize stemming and lemmatization are technique used for text processing in NLP"),
    ("The stemming approach is much faster than lemmatization","The stemming approach is much faster than lemmatization")
])
def test_transform_lemmatizer(text, expected):
    assert transform_lemmatizer(text) == expected

if __name__ == "__main__":
    pytest.main()
