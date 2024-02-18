========
 libzet
========
Hello and welcome to libzet, a library for managing zettels.

Building and installation
=========================
Available from PyPi; Just ``pip3 install libzet``

Alternatively, clone this repo and then pip3 install.

::

    pip3 install --user .

Testing
=======
Use the following command to run unit tests.

::

    python3 -m unittest

Maintenance and versioning
==========================
Update the CHANGELOG and version in pyproject.toml when cutting a release.
Build with ``make`` and use ``make release`` to upload to pypi.

Usage
=====
The libzet library provides functions to parse zettels out of Markdown
or RST text formats and manage these zettels on the filesystem.

Zettel File Format
------------------
Zettels may be stored in markdown or RST format. Each may have a title,
content, and metadata in yaml format. The metadata is stored at the bottom
because metadata blocks can grow quite large.

Here's an example in markdown.

::

    # Markdown Zettel Title

    Some content

    ## Heading 1
    Notes under Heading 1

    <!--- attributes --->
        ---
        creation_date: 2023-03-09
        zlinks: {}

And an example in RST.

::
    
    ==================
     RST Zettel Title
    ==================
    Some content

    Heading 1
    =========
    Notes under Heading 1

    .. attributes
    ::

        ---
        creation_date: 2023-03-09
        zlinks: {}

Zettel Class
------------
Text formatted as above may be parsed into Zettel objects.

- ``zettel.title``: Title of the zettel.
- ``zettel.headings``: Dictionary of level-2 headings within the zettel. The
  content immediately under the title is in the ``_notes`` key.
- ``zettel.attrs``: Attributes of the Zettel.

The ``attrs`` is a dictionary that will automatically parse date fields. Any
key with the word 'date' in it will be parsed. Dates read in this matter may
be very free-form. Plain English phrases such as "tomorrow" or
"next Wednesday" should work fine.

Parsing and printing
--------------------
Zettels can be parsed out of a string with the ``str_to_zettels`` function, and
then printed using the ``zettels_to_str`` function or the zettel's own
``getMd()`` or ``getRst()`` methods.

::

    def str_to_zettels(text, zettel_format):
        """ Convert a str to a list of zettels.
    
        This function's return may be passed to zettels_to_str.
    
        Args:
            text: Text to convert to zettels.
            zettel_format: 'rst' or 'md'.
    
        Returns:
            A list of Zettel references.
    
        Raises:
            ValueError if the text was invalid.
        """
    
    
    def zettels_to_str(zettels, zettel_format, headings=None):
        """ Return many zettels as a str.
    
        This function's return may be passed to str_to_zettels.
    
        Args:
            zettels: List of zettels to print.
            zettel_format: 'rst' or 'md'.
            headings: Only print select headings.
    
        Returns:
            A str representing the zettels.
        """

Filesystem management
---------------------
Libzet provides functions to assist with managing zettels on the filesystem.

- Create a new zettel on disk with ``create_zettel``
- Load a list of zettels from disk with ``load_zettels``
- Filter this list based on the needs of your application.
- Modify the zettels and save the changes with ``save_zettels``
- Or send them to ``edit_zettels`` to edit them in a text editor.
- Move zettels around using ``copy_zettels`` or ``move_zettels``
- Remove unwanted zettels with ``delete_zettels``

These functions each return valid zettel references with respect to their
locations on disk. The general idea for an application is to keep track
of its zettels using the return values of these functions.

A zettel's location on disk is tracked with a ``_loadpath`` attribute. These
functions will automatically manage this attribute, so ensure it is not
carelessly modified in flight.

::

    def create_zettel(
            path,
            text='', title='', headings=None, attrs=None, zettel_format='md',
            no_edit=False, errlog='', template=None):
        """ Create and new zettel on disk and edit it.
    
        Args:
            path: Path to create new zettel.
            text: Provide a body of text from which to parse the whole zettel.
            headings: Headings to create the new zettel with.
            attrs: Default attributes to create the zettel.
            zettel_format: 'md' or 'rst'
            errlog: See edit_zettels
            no_edit: Set to True to skip editing.
            template: Optionally init the new zettel from a template. May be
                a path to a yaml file or a dict. Defaults to ztemplate.yaml
                within the same dir as the new zettel.
    
                If template exists then the headings and attrs from that
                file will be used to init the zettel.
    
        Returns:
            The new zettel reference.
    
        Raises:
            FileExistsError: There was already a zettel at path.
            ValueError: The newly created zettel was invalid.
        """
    
    
    def load_zettels(paths, zettel_format='md', recurse=False):
        """ Load Zettels from the filesystem.
    
        Zettels will be updated with a _loadpath value in their attrs.
        Send these zettels to save_zettels after modifying them to write
        them to disk. The _loadpath attribute will not be written to disk.
    
        Args:
            paths: Path or list paths to zettels. Each may be a dir or file.
            zettel_format: md or rst
            recurse: True to recurse into subdirs, False otherwise.
    
        Returns:
            A list of zettels.
    
            This list may be passed to save_zettels to write
            them to the filesystem.
    
        Raises:
            OSError if one of the files couldn't be opened.
            ValueError if one of the zettels contained invalid text.
        """
    
    
    def edit_zettels(zettels, zettel_format='md', headings=None, errlog='', delete=False):
        """ Bulk edit zettels provided by load_zettels.
    
        Delete the text for a zettel to avoid updating it.
    
        It is possible to add new zettels while editing, just be sure
        to set the _loadpath attribute for each new zettel.
    
        Args:
            zettels: List of zettels to edit.
            zettel_format: md or rst.
            headings: Only edit specific headings for each zettel.
            errlog: Write your working text to this location if parsing failed.
            delete: If True, then zettels whose text is deleted during editing will
                also be deleted from the disk.
    
        Returns:
            A list of zettels that were updated. Deleted zettels will not be
            in this list.
    
        Raises:
            ValueError if any zettels were edited in an invalid way.
        """
    
    
    def save_zettels(zettels, zettel_format='md'):
        """ Save zettels back to disk.

        the _loadpath attribute will not be written.
    
        Args:
            zettels: List of zettels.
            zettel_format: md or rst.
    
        Returns:
            The list of zettels as saved to disk.
    
        Raises:
            KeyError if a zettel is missing a _loadpath attribute. No zettels
                will be written to disk if this is the case.
    
            OSError if a zettel's text couldn't be written to disk.
        """
    
    
    def delete_zettels(zettels):
        """ Delete zettels from the filesystem.
    
        Args:
            zettels: Zettels to delete. Must have a _loadpath attribute.
    
        Returns:
            An empty list to represent the loss of these zettels
    
        Raises:
            KeyError if any zettels were missing a _loadpath. No zettels
                will be deleted in this case.
    
            OSError if the zettel could not be deleted.
        """
    
    
    def copy_zettels(zettels, dest, zettel_format='md'):
        """ Copy zettels to a new file location.
    
        Zettels are saved to disk before copying.
    
        Args:
            zettels: List of zettels to copy.
            zettel_format: md or rst.
            dest: Location to copy them to.
    
        Returns:
            A list of the new zettels loaded from their new file locations.
    
        Raises:
            KeyError if any zettels were missing a _loadpath. No zettels
                will be written to disk in this case.
    
            OSError if any of the zettels failed to copy.
    
            See shutil.copy
        """
    
    
    def move_zettels(zettels, dest, zettel_format='md'):
        """ Move zettels. Zettels will be saved before moving.

        The zettels will be deleted from their former paths which
        invalidates their previous _loadpath. Use this function like...

            zettels = move_zettels(zettels, './new-dir/')
    
        Args:
            zettels: List of zettels to move.
            zettel_format: md or rst.
            dest: Destination directory.
    
        Returns:
            A list of the zettels from their new home.
    
        Raises:
            See copy_zettels and delete_zettels.
        """
