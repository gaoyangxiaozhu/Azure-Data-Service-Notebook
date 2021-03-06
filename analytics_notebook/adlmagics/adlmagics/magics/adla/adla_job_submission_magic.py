from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from magics.adla.adla_magic_base import AdlaMagicBase
from models.adla_job_submission import AdlaJobSubmission

class AdlaJobSubmissionMagic(AdlaMagicBase):
    def __init__(self, adla_service):
        super(AdlaJobSubmissionMagic, self).__init__("submitjob", adla_service)

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake account name.")
    @argument("--name", type = str, help = "Azure data lake job name.")
    @argument("--parallelism", type = int, help = "Azure data lake job parallelism.")
    @argument("--priority", type = int, help = "Azure data lake job priority.")
    @argument("--runtime", type = str, help = "Azure data lake job runtime.")
    def execute(self, arg_string, content_string):
        args = parse_argstring(self.execute, arg_string)

        job_submission = AdlaJobSubmission(args.name, content_string, args.parallelism, args.priority, args.runtime)

        self._write_line("Submitting azure data lake job to account '%s'..." % (args.account))

        job = self._adla_service.submit_job(args.account, job_submission)

        self._write_line("Job submitted.")
        self._write_line("\tId: %s" % (job.id))
        self._write_line("\tName: %s" % (job.name))
        self._write_line("\tType: %s" % (job.type))
        self._write_line("\tSubmitter: %s" % (job.submitter))
        self._write_line("\tParallelism: %d" % (job.parallelism))
        self._write_line("\tPriority: %d" % (job.priority))
        self._write_line("\tSubmit time: %s" % (str(job.submit_time)))
        self._write_line("\tStart time: %s" % (str(job.start_time)))
        self._write_line("\tEnd time: %s" % (str(job.end_time)))
        self._write_line("\tState: %s" % (job.state))
        self._write_line("\tResult: %s" % (job.result))

        return job