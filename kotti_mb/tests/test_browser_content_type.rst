kotti_mb browser tests
============================

Setup and Login
---------------

  >>> from kotti import testing
  >>> tools = testing.setUpFunctional(
  ...     **{'kotti.configurators': 'kotti_mb.kotti_configure'})
  >>> browser = tools['Browser']()
  >>> ctrl = browser.getControl

  >>> browser.open(testing.BASE_URL + '/@@login')
  >>> "Log in" in browser.contents
  True
  >>> ctrl("Username or email").value = "admin"
  >>> ctrl("Password").value = "secret"
  >>> ctrl(name="submit").click()
  >>> "Welcome, Administrator" in browser.contents
  True


Add a ContentType
--------------

  >>> browser.open(testing.BASE_URL + '/@@add_content_type')
  >>> ctrl("Title").value = "New Content Type"
  >>> ctrl("Description").value = "This is a Content Type"
  >>> ctrl("Example Text").value = u"The new text"
  >>> ctrl("save").click()
  >>> browser.url == testing.BASE_URL + '/new-content-type/'
  True
  >>> "Successfully added item" in browser.contents
  True


View ContentType
-------------

  >>> browser.open(testing.BASE_URL + '/new-content-type/')
  >>> "This is a Content Type" in browser.contents
  True


Edit ContentType
-------------

  >>> browser.open(testing.BASE_URL + '/new-content-type/@@edit')
  >>> "Edit <em>New Content Type</em>" in browser.contents
  True
