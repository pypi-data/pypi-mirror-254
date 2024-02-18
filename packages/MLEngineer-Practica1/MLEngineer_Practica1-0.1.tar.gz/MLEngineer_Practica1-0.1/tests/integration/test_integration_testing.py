import pytest
from processing import *
import numpy as np

@pytest.mark.parametrize("test_input,expected", 
                         [("We will, we will rock you We will, we will rock you Buddy, you're a young man, hard man", np.array([4, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]))])
                          
def test_bar_plot_values(test_input, expected):
    bar_plot_input, bar_plot_test = bar_plot(remove_characters(test_input))
    assert (bar_plot_test == expected).all()
    
@pytest.mark.parametrize("test_input,expected", 
                         [("We will, we will rock you We will, we will rock you Buddy, you're a young man, hard man", ['will','We','we','rock','you','man','Buddy','youre','a','young','hard'])])

def test_bar_plot_names(test_input, expected):
    bar_plot_input, bar_plot_test = bar_plot(remove_characters(test_input))
    assert bar_plot_input == expected

@pytest.mark.parametrize("test_input,expected", 
                         [("Don't stop me now, I'm having such a good time I'm having a ball Don't stop me now", 33)])       
def test_pie_chart_names(test_input, expected):
    assert len(pie_chart(remove_characters(test_input))) == expected

@pytest.mark.parametrize("test_input,expected", 
                         [("Often said when things are still not decided. Plans still need to be finalized.", [1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])])
def test_cloud_words(test_input, expected):
    cw = list(cloud_words(remove_characters(test_input)).words_.values())
    assert cw == expected

@pytest.mark.parametrize("test_input,expected", 
                         [("Never give in. Never give in. Never, never, never, never-in nothing, great or small, large or petty-never give in, except to convictions of honor and good sense.", 7)])
def test_plot_word_frequency(test_input, expected):
    wf = len(plot_word_frequency(remove_characters(test_input)).gca().get_yticklabels())
    assert wf == expected

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Check out this #awesome link: http://example.com", "Check out this  link: "),
        ("No hashtags or links here!", "No hashtags or links here!"),
        (123, 123),  
    ],
)
def test_remove_hashtags_and_links(input_text, expected_output):
    processed_text = remove_hastags(remove_links(input_text))
    assert processed_text == expected_output
    
    
@pytest.mark.parametrize("input_text, expected_output", [
    ("Testing @user123 regex 456removal", "Testing  regex removal"),
    ("No changes needed", "No changes needed"),
    ("1234567890", ""),
    ("@user1 @user2 @user3", '  '),
])
def test_remove_numbers_and_users(input_text, expected_output):
    processed_text = remove_numbers(remove_users(input_text))
    assert processed_text == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
    ("Python programmers often tend like programming in python. This is the link: https://example.com", "python programm often tend like program in python thi is the link")
])
def test_remove_links_and_stemmer_transform(input_text, expected_output):
    processed_text = transform_stemmer(remove_links(input_text))
    assert processed_text == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
    ("Just finished an amazing workout session 123abc456def789", "Just finished an amazing workout session abcdef")
])
def test_remove_numbeers_and_lemmatizer_transform(input_text, expected_output):
    processed_text = transform_lemmatizer(remove_numbers(input_text))
    assert processed_text == expected_output


if __name__ == "__main__":
    pytest.main()