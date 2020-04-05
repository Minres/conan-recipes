#include <cassert>
#include "rocksdb/db.h"

int main()
{
  rocksdb::DB * db;
  rocksdb::Options options;

  options.create_if_missing = true;

  rocksdb::Status status = rocksdb::DB::Open(options, "/tmp/testrocksdb", &db);

  assert(status.ok());

  return 0;
}
