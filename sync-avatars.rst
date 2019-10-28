sync-avatars
============

Synchronize employees's avatars on schedule.

Quickstart
==========

.. _1-pre-work:

1. Pre-work
-----------

.. _1-install-dlib:

1) Install ``dlib``
~~~~~~~~~~~~~~~~~~~

::

   ./depends/install-dlib.sh

If there are some errors, please refer to `How to install dlib v19.9 or
newer (w/ python bindings) from github on macOS and Ubuntu`_ for
installation

.. _2-install-pillow-simd:

2) Install ``pillow-simd``
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   ./depends/install-pillow-simd.sh

.. _3-then-install-packages-from-requirementstxt:

3) Then install packages from ``requirements.txt``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   pip install -r requirements.txt

.. _2-usage:

2. usage
--------

.. _1-create-a-sqlite-db-before-the-first-run:

1). Create a sqlite db before the first run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   python run.py create

.. _2-sync-avatars:

2). Sync avatars
~~~~~~~~~~~~~~~~

**Run once**

::

   python run.py run

**Or run everyday at ``00:30``**

::

   python run.py schedule -a 00:30

.. _3-help:

3. Help
-------

::

   >>> python run.py --help
   Usage: run.py [OPTIONS] COMMAND [ARGS]...

   Options:
     --help  Show this message and exit.

   Commands:
     create    Create all tables.
     drop      Drop all tables.
     run       Run app to sync avatars.
     schedule  Run a scheduling job.

Run via docker
==============

.. _1-build-image:

1. Build image
--------------

::

   docker build -t lonsty/sync_avatars:latest -f Dockerfile .

.. _2-custom-a-volume-mount-to-avatars-folder:

2. Custom a volume mount to avatars folder
------------------------------------------

::

   docker volume create --driver local --opt type=none --opt device=/mnt/data/workspace/sync-avatars/resources --opt o=bind avatars_vol

.. _3-start-a-container-with-avatars-volume:

3. Start a container with avatars volume
----------------------------------------

::

   docker run -d --name sync_avatars --mount src=avatars_vol,target=/root/sync_avatars/resources lonsty/sync_avatars:latest

Rsync avatars to production server
==================================

Add job to crontab file
~~~~~~~~~~~~~~~~~~~~~~~

::

   sudo vi /etc/crontab

..

   17 1 \* \* \* root sshpass -p "Fox@0000" rsync -av -e "ssh -p 65535"
   /mnt/data/workspace/sync-avatars/resources
   admin@10.132.166.121:/home/admin/temp

Add job to crontab schedule
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   crontab -u root /etc/crontab

Restart crontab service
~~~~~~~~~~~~~~~~~~~~~~~

::

   sudo service cron reload
   sudo service cron restart

Release History
===============

.. _version-010-2019-09-18:

Version 0.1.0 (2019-09-18)
--------------------------

New Features:
~~~~~~~~~~~~~

-  Used ``pillow-simd`` to improve image processing performance.
-  Used built-in method ``Image.thumbnail`` to thumbnail image.

.. _version-010a-2019-09-12:

Version 0.1.0a (2019-09-12)
---------------------------

Features:
~~~~~~~~~

-  Synchronize employees's avatars on schedule.
-  Used face recognition to crop face from avatars of different sizes,
   and used same trick to improve performance.
-  The sync will be more faster after first run, because it's a
   incremental synchronization.

.. _How to install dlib v19.9 or newer (w/ python bindings) from github on macOS and Ubuntu: https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf
