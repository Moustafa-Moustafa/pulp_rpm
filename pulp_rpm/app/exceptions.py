from gettext import gettext as _

from pulpcore.plugin.exceptions import PulpException


class AdvisoryConflict(PulpException):
    """
    Raised when two advisories conflict in a way that Pulp can't resolve it.
    """

    def __init__(self, msg):
        """
        Set the exception identifier.

        Args:
            msg(str): Detailed message about the reasons for Advisory conflict
        """
        super().__init__("RPM0001")
        self.msg = msg

    def __str__(self):
        """
        Return a message for the exception.
        """
        return self.msg


class DistributionTreeConflict(FileNotFoundError):
    """
    Raised when two or more distribution trees are being added to a repository version.
    """

    def __init__(self, msg):
        """
        Set the exception identifier and msg.
        """
        super().__init__("RPM0002")
        self.msg = _("More than one distribution tree cannot be added to a " "repository version.")

    def __str__(self):
        """
        Return a message for the exception.
        """
        return self.msg


class UlnCredentialsError(PulpException):
    """
    Raised when no valid ULN Credentials were given.
    """

    def __init__(self, msg):
        """
        Set the exception identifier and msg.
        """
        super().__init__("RPM0003")
        self.msg = _("No valid ULN credentials given.")

    def __str__(self):
        """
        Return a message for the exception.
        """
        return self.msg
