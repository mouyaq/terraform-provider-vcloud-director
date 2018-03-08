# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import org_pb2 as proto_dot_org__pb2


class OrgStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/proto.Org/Create',
        request_serializer=proto_dot_org__pb2.CreateOrgInfo.SerializeToString,
        response_deserializer=proto_dot_org__pb2.CreateOrgResult.FromString,
        )
    self.Delete = channel.unary_unary(
        '/proto.Org/Delete',
        request_serializer=proto_dot_org__pb2.DeleteOrgInfo.SerializeToString,
        response_deserializer=proto_dot_org__pb2.DeleteOrgResult.FromString,
        )
    self.Read = channel.unary_unary(
        '/proto.Org/Read',
        request_serializer=proto_dot_org__pb2.ReadOrgInfo.SerializeToString,
        response_deserializer=proto_dot_org__pb2.ReadOrgResult.FromString,
        )
    self.Update = channel.unary_unary(
        '/proto.Org/Update',
        request_serializer=proto_dot_org__pb2.UpdateOrgInfo.SerializeToString,
        response_deserializer=proto_dot_org__pb2.UpdateOrgResult.FromString,
        )


class OrgServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    """create a organisation
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """delete a organisation
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Read(self, request, context):
    """Read Org
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update org
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OrgServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=proto_dot_org__pb2.CreateOrgInfo.FromString,
          response_serializer=proto_dot_org__pb2.CreateOrgResult.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=proto_dot_org__pb2.DeleteOrgInfo.FromString,
          response_serializer=proto_dot_org__pb2.DeleteOrgResult.SerializeToString,
      ),
      'Read': grpc.unary_unary_rpc_method_handler(
          servicer.Read,
          request_deserializer=proto_dot_org__pb2.ReadOrgInfo.FromString,
          response_serializer=proto_dot_org__pb2.ReadOrgResult.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=proto_dot_org__pb2.UpdateOrgInfo.FromString,
          response_serializer=proto_dot_org__pb2.UpdateOrgResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.Org', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
