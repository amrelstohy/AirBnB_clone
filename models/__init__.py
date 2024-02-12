
"""
package init module
"""
from .engine.file_storage import FileStorage
""""
create a unique FileStorage instance for application
"""
storage = FileStorage()
storage.reload()