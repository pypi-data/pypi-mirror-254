# POI Tracker

Tool for keeping track of packages of interest

## Rationale

The set of packages a user might be interested in are not identical to the set
of packages they have access to, even within a distribution's main repository:

- sysadmins who are not package maintainers for the distribution they use, by
  definition, don't have commit access to change the packages they use
- package maintainers would have dependencies maintained by other packagers,
  that they want to keep track of
- not all packages are equal: e.g. a packager might maintain some packages for
  work use, and some for personal use; some might need to be updated more
  frequently or are more likely to be exposed to security issues
- leaf packages vs non-leaf packages - for the latter a packager would be
  interested in the dependent packages that have to be tested or rebuilt

Once multiple repositories are involved, the situation gets even more complex:

- source of truth for bugs and issues - e.g.
  - RH's JIRA (RHEL and CentOS Stream)
  - RH's Bugzilla (Fedora and EPEL)
  - etc.

Sysadmins and power users might also be interested in the same set of packages
across different distributions, likewise with upstream software developers who
are interested in tracking their software (and dependents and dependencies) as
packaged in these distributions
