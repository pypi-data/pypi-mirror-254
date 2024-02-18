==========================
eea.jupyter
==========================
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.jupyter/develop
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.jupyter/job/develop/display/redirect
  :alt: Develop
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.jupyter/master
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.jupyter/job/master/display/redirect
  :alt: Master

The eea.jupyter is a jupyter utility package for EEA.

.. contents::

Upgrade
=======


Usage
=============
1. Install eea.jupyter package
  
.. code-block:: console

  pip install eea.jupyter

2. Import PlotlyController in your notebook
  
.. code-block:: python

  from eea.jupyter.controllers.plotly import PlotlyController

3. Create a PlotlyController instance

.. code-block:: python

  plotlyCtrl = PlotlyController(url)

4. Upload a plotly figure

.. code-block:: python

  plotlyCtrl.uploadPlotly(chart_data, metadata)

Note: step 3 should be run as the last part of notebook cell, otherwise the plotly editor will not be displayed in the notebook.


Install
=======


Eggs repository
===============

- https://pypi.python.org/pypi/eea.jupyter
- http://eggrepo.eea.europa.eu/simple


How to contribute
=================
See the `contribution guidelines (CONTRIBUTING.md) <https://github.com/eea/eea.jupyter/blob/main/CONTRIBUTING.md>`_.


Copyright and license
=====================

eea.jupyter (the Original Code) is free software; you can
redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc., 59
Temple Place, Suite 330, Boston, MA 02111-1307 USA.

The Initial Owner of the Original Code is European Environment Agency (EEA).
Portions created by Eau de Web are Copyright (C) 2009 by
European Environment Agency. All Rights Reserved.


Funding
=======

EEA_ - European Environment Agency (EU)

.. _EEA: https://www.eea.europa.eu/
.. _`EEA Web Systems Training`: http://www.youtube.com/user/eeacms/videos?view=1
