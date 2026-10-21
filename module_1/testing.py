import pytest 
import square_turtle as sqt

def test_number_of_segments():
    
    """
    GIVEN a number of sides and their lenght
    WHEN generate_segments is called
    THEN the list returned should have the same number of elements as the number of sides
    """
    
    sides = 4
    length = 100

    result = sqt.generate_segments(sides, length)
    
    assert len(result) == sides
  
def test_all_segments_equal():
  """
  GIVEN a number of sides and their lenght
  WHEN generate_segments is called
  THEN all the segments returned should have the same lenght and all the angles should be equal
  """

  sides = 6
  length = 100

  result = sqt.generate_segments(sides,length)

  for angle, distance in result:
    assert distance == pytest.approx(length)
    assert angle == pytest.approx(360/sides)

