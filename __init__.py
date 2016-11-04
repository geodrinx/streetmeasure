# -*- coding: utf-8 -*-
"""
/***************************************************************************
 streetmeasure
                                 A QGIS plugin
 streetmeasure
                             -------------------
        begin                : 2016-11-04
        copyright            : (C) 2016 by geodrinx
        email                : geodrinx@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load streetmeasure class from file streetmeasure.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .streetmeasure import streetmeasure
    return streetmeasure(iface)
