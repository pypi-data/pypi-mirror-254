~~~~~~~~~~~~~~~~~~~~~
FletNavigator V2.6.5
~~~~~~~~~~~~~~~~~~~~~

.. image :: https://github.com/xzripper/flet_navigator/raw/main/example2.gif
   :width: 500

FletNavigator & `FletReStyle <https://github.com/xzripper/flet_restyle>`_

Simple and fast navigator (router) for Flet (Python) that allows you to create multi-page applications!

Click `here <https://github.com/xzripper/flet_navigator/blob/main/flet-navigator-docs.md>`_ for documentation.

Using Example:

.. code :: python

   from flet import app, Page, Text

   from flet_navigator import VirtualFletNavigator, PageData, ROUTE_404, route


   @route('/')
   def main_page(pg: PageData) -> None:
      pg.add(Text('Main Page!')) # or pg.page.add

   @route('second_page')
   def second_page(pg: PageData) -> None:
      ... # Second page content.

   @route(ROUTE_404)
   def route_404(pg: PageData) -> None:
      ... # 404 Page Content.

   def main(page: Page) -> None:
      # Initialize navigator and render page.
      VirtualFletNavigator().render(page)

   app(main)

.. image :: https://raw.githubusercontent.com/xzripper/flet_navigator/main/example.gif
   :width: 400

(Deprecated Example GIF).

See the difference between `VirtualFletNavigator` and `FletNavigator`, and more `here <https://github.com/xzripper/flet_navigator/blob/main/flet-navigator-docs.md>`_ (<- documentation).

-----------------------------------------------

   FletNavigator V2.6.5
