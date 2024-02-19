# sftputil

Python High-level SFTP client library

Documentation is available on [readthedocs](https://sftputil.readthedocs.io),
or in [docs/index.md](./docs/index.md).

## Description

`sftputil` is Python library to transfer files using SFTP. At this point only
the API is available, but a command line will probably be added in the future.

Why this package?

- Paramiko provides a
  [SFTP](https://docs.paramiko.org/en/latest/api/sftp.html#paramiko.sftp_client.SFTPClient)
  client but it does not contain many methods. It is alright if one only needs
  simple get/put/list commands. But it is not enough for more complex operations.
- [pySFTP](https://pypi.org/project/pysftp/) would have been the solution, but
  it has not been updated since 2016 (at the time of this writing). It is a dead
  project and cannot be improved. It does not manage the last SSH key
  algorithms.

Thus this new project. The initial reason was also that I needed a `rsync`-like
command through SFTP in Python scripts.

## Installation

Available on [pypi](https://pypi.org/project/sftputil/).

```
pip install sftputil
```

## Usage

TODO

## Support

If you have any question or suggestion, you can open a new
[issue](https://framagit.org/RomainTT/sftputil/-/issues).

## Roadmap

TODO for future releases:

- Add synchronisation on the other direction (push)
- Add a command line
- Add some unit tests

## Contributing

You are free to fork this repository and to do Merge Requests that I will
review.

## Authors and acknowledgment

Main author: Romain TAPREST <romain@taprest.fr>

## License

Licensed under [Mozilla Public License v2](./LICENSE).

## Project status

Alive! 💓
