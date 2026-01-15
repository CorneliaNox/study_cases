class ProductsPage:
  def __init__(self):
    self.header = HeaderComponent()
    self.breadcrumbs = BreadcrumbsComponent()
    self.product_filters = ProductFiltersComponent()
    self.product_grid = ProductGridComponent()


class HeaderComponent:
  def __init__(self):
    pass


class BreadcrumbsComponent:
  def __init__(self):
    pass


class ProductFiltersComponent:
  def __init__(self):
    pass

  def select_category(self, category: str):
    pass


class ProductGridComponent:
  def __init__(self):
    self.sorting = SortingComponent()
    self.filter_tags = FilterTagsComponent()
    self.product_items = ProductItemComponent()

  def find_product(self, product_name: str):
    pass


class FilterTagsComponent:
  def __init__(self):
    pass


class SortingComponent:
  def __init__(self):
    pass


class ProductItemComponent:
  def __init__(self):
    pass

  def add_to_cart(self):
    pass

  def is_in_cart(self):
    pass


class TestCase:
  def __init__(self):
    self.products_page = ProductsPage()

  # AAA - Arrange, Act, Assert

  def add_product_to_cart(self):
    product_slug = mocks.get_product_slug()
    product_category = api.get_product_category({ "product_slug": product_slug})

    self.products_page.product_filters.select_category(product_category)

    # Scenario

    assert self.products_page.product_filters.is_category_selected(product_category)

    assert self.products_page.product_grid.is_product_available()

    product = self.products_page.product_grid.find_product(product_name)

    product.add_to_cart()

    assert product.is_in_cart()