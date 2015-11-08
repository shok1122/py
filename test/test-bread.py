import bread as b
import sys

enum_data_type = [
		("type", b.enum(8, {
			0x50 : "raw",
			0x51 : "enc"
		}))
]

hex_data = [
		("data", b.array(5, b.byte), {"str_format": hex})
]

str_data = [
		("type", b.enum(8, {
			0x50 : "raw",
			0x51 : "enc"
		})),
		("data", b.array(5, b.byte), {"str_format": hex})
]

data = bytearray([0x51, 0x01, 0x02, 0x03, 0x04, 0x05])
parsed_data = b.parse(data, str_data)
print parsed_data

simple_spec_hex = [('addr', b.uint8, {"str_format": hex})]
parsed_data = b.parse(bytearray([42]), simple_spec_hex)
print parsed_data

