# Logs Analysis

This Python project connects to a PostgreSQL database and runs analyses of the
news website logs in to answer three questions. I've created this program as
part of the [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Running the Program

1. You'll need to download [the Vagrant configuration Udacity has provided](https://github.com/udacity/fullstack-nanodegree-vm), and must have
Vagrant and VirtualBox set up on your system.

1. From the `vagrant` directory, run `vagrant up` to setup the virtual machine.

1. Fork, clone or download this repository into the `vagrant` directory.

1. Download and unzip [the script to generate the data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and save the file in the `vagrant` directory.

1. Now you're ready to connect to the virtual machine and setup the database:

    1. `vagrant ssh`

    1. `cd /vagrant` (and if you put the files into a subdirectory, `cd` to it)

    1. `psql -d news -f newsdata.sql`

1. You can explore the database using `psql -d news` if you want to check out
its structure and contents.

1. Run `python3 logs_analysis.py` to execute and output the analysis.
