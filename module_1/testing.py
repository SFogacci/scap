import pytest 
import square_turtle as sqt
import math

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

def test_radius_distance():
  """
  GIVEN a number of side and a center
  WHEN center_to_vertex
  THEN the distance center-output is equal to the radius
  """

  sides = 5
  length = 100
  x_cen = 10
  y_cen = 20

  x_ver, y_ver = sqt.center_to_vertex(x_cen, y_cen, 0, length, sides)
  distance = math.sqrt((x_ver-x_cen)**2+ (y_ver-y_cen)**2)
  radius = length / (2*math.sin(math.pi/sides))
  
  assert radius == pytest.approx(distance)


def test_number_of_vertexes():
  """
  GIVEN a number of sides
  WHEN vertexes_position is called
  THEN the number of vertex shoud correspond to the number of sides
  """

  sides = 9

  vertexes = sqt.vertexes_position(0,0,0,0,sides)

  assert len(vertexes) == sides


def test_vertexes_center_distance():
  """
  GIVEN a number of sides and a center
  WHEN vertexes_position is called
  THEN the distance center vertex must be eual for all vertexes
  """

  sides = 7
  length = 100
  x_cen = 200
  y_cen = 300
  vertexes = sqt.vertexes_position(x_cen, y_cen, 0, length, sides)
  distance = [ math.sqrt((x_cen-x_ver)**2+(y_cen-y_ver)**2) for x_ver,y_ver in vertexes]
  
  for i in range(sides-1):

    assert distance[0] == pytest.approx(distance[i+1])
