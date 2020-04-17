# python 3
# create a class

class new_bit(object):

  def __init__(self, serial, size, bit_type):
    self.serial=serial
    self.size=size
    self.bit_type=bit_type
  
  def details(self):
    print('Serial\t', self.serial, '\n', 'Size\t', self.size, '\n', 'Type\t',self.bit_type)
