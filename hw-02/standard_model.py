"""Module containing the elementary particle classes. """

import numpy as np

# +
"""Module containing the elementary particle classes. """

import numpy as np


class ElementaryParticle:
    """ Elementary particle class.
    Attributes
    ----------
    x : float
        x-position of the particle.
    y: float
        y-position of the particle.
    ptype: str
        Statistics obeyed by the particle.
    charge : float
        Electric charge of the particle.
    mass : float
        Rest mass in MeV of the particle.
    spin: float
        Spin of the particle.
    Methods
    -------
    info():
        Prints particles information.
    is_antiparticle(other):
        Check if the other is this particle anti-particle
    move()
        Move the particle randomly.
    place_at(coord):
        Place the particle at passed coord.
    """
    x = None
    y = None
    ptype=None
    
    def __init__(self, charge, mass, spin):
        """Initialize the particle's attributes.
        Parameters
        ----------
        charge : float
            Electric charge of the particle.
        mass : float
            Rest mass in MeV of the particle.
        spin: float
            Spin of the particle.
        """
        self.charge = charge
        self.mass = mass
        self.spin = spin
        
        

    def info(self):
        """Print to scree information about the particle."""

        print(f"The particle has a mass of {self.mass} MeV")
        print(f"The particle's charge is {self.charge} e")
        print(f"The particle's spin is {self.spin}")

    def place_at(self, coord):
        """Place particles at coordinates (x,y).
        Parameters
        ----------
        coord: tuple
            (x,y) coordinates where to place the particle.
        """
        self.x = coord[0]
        self.y = coord[1]

    def move(self):
        """Move the particle by randomly pushing it in both directions."""
        self.x += np.random.randint(low=-1, high=2)
        self.y += np.random.randint(low=-1, high=2)
    
    def check_type(self):
        """Checks if type is boson or fermion"""
        if self.spin.is_integer():
            ptype = "boson"
        else:
            ptype = "fermion"
        return ptype
    
    def compare(self, other):
        """Compares the charge, mass and spin of the other particle
        
        Parameters
        ----------
        other: ElementaryParticle
        """
        if isinstance(other, ElementaryParticle):
            if self.charge == other.charge:
                print("The two particles have the same charge: True")
            else:
                print("The two particles have the same charge: False")
                
            if self.mass == other.mass:
                print("The two particles have the same mass: True")
            else:
                print("The two particles have the same mass: False")
                
            if self.spin == other.spin:
                print("The two particles have the same spin: True")
            else:
                print("The two particles have the same spin: False")     
        else:
            raise TypeError("Not a particle")


# -

class Boson(ElementaryParticle):
    """
    Boson: elementary particle that obeys Bose-Einstein statistics.
    This class inherits the ElementaryParticle class with all its attributes and methods.
    Further attributes and methods are
    Attributes
    ----------
    name: str
    Name of the particle.
    Methods
    -------
    check_existence()
    Checks whether this Boson can exists by calling its parent's method check_type()
    Raises a ValueError if check_type() returns "fermion"
    """
    def __init__(self, name, charge, mass, spin):
        self.name = name
        ptype = "boson"
        super().__init__(charge, mass, spin)
    
    def check_existence(self):
        if self.check_type() == "fermion":
            raise ValueError("This particle cannot exist")
        else:
            print("This particle can exist")



# +
class Fermion(ElementaryParticle):
    """
    Fermion: elementary particle that obeys Fermi-Dirac statistics.
    This class inherits the ElementaryParticle class with all its attributes and methods.
    Further attributes and methods are
    Attributes
    ----------
    name: str
    Name of the particle.
    Methods
    -------
    check_existence()
    Checks whether this Fermion can exists by calling its parent's method check_type()
    Raises a ValueError if the check_type() returns "boson"
    is_antiparticle(other):
    Check whether other is the anti-particle of this Fermion 
    by checking if other is an instance of Fermion first.
    """
    def __init__(self, name, charge, mass, spin):
        self.name = name
        ptype = "Fermion"
        super().__init__(charge, mass, spin)

    def check_existence(self):
        if self.check_type() == "boson":
            raise ValueError("This particle cannot exist")
        else:
            print("This particle can exist")

    def is_antiparticle(self, other):
        if isinstance(other, Fermion) and self.charge == -other.charge:
            return True
        else:    
            return False
        
#            raise TypeError("Not a particle")



# -

class CompositeParticle(ElementaryParticle):
    """
    A particle composed of several elementary particles.
    Parameters
    ----------
    name: str
        Name of the particle.
    particles : list
        List of particles objects that compose this particle.
    charge : float
        Electric charge of the particle.
    mass : float
        Rest mass in MeV of the particle.
    spin: float
        Spin of the particle.
    """
    def __init__(self, name, particles):
        self.name = name
        self.particles = particles
        
        self.charge = self.mass = self.spin = 0
        for particle in self.particles:
            self.charge += particle.charge
            self.mass += particle.mass
            self.spin += particle.spin


