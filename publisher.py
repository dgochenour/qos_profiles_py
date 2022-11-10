"""
 (c) 2022 Copyright, Real-Time Innovations, Inc.  All rights reserved.
 RTI grants Licensee a license to use, modify, compile, and create derivative
 works of the Software.  Licensee has the right to distribute object form only
 for use with RTI products.  The Software is provided "as is", with no warranty
 of any type, including any warranty for fitness for any purpose. RTI is under
 no obligation to maintain or support the Software.  RTI shall not be liable for
 any incidental or consequential damages arising out of the use or inability to
 use the software.
 """

import rti.connextdds as dds
import time
import argparse
import random


def publisher_main(domain_id, sample_count):
    qos_provider = dds.QosProvider("./my_qos.xml")
    participant = dds.DomainParticipant(domain_id, qos=qos_provider.participant_qos_from_profile("MyLibrary::MyProfile"))

    my_type = dds.QosProvider("./my_types.xml").type("my_type_lib", "Pose")
    topic = dds.DynamicData.Topic(participant, "Example Topic", my_type)
    writer = dds.DynamicData.DataWriter(dds.Publisher(participant), topic, qos_provider.datawriter_qos_from_profile("MyLibrary::MyProfile"))

    sample = dds.DynamicData(my_type)
    sample["obj_id"] = 10 #arbitrary ID
    count = 0
    while (sample_count == 0) or (count < sample_count):
        print("Writing Pose, count = {}".format(count))
        sample["position.x"] = random.random()
        sample["position.y"] = random.random()
        sample["position.z"] = random.random()        
        writer.write(sample)

        count += 1
        time.sleep(0.1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="RTI Connext DDS Example: Waitsets with Status Condition & Read Condition (Publisher)"
    )
    parser.add_argument("-d", "--domain", type=int, default=0, help="DDS Domain ID")
    parser.add_argument(
        "-c", "--count", type=int, default=0, help="Number of samples to send"
    )

    args = parser.parse_args()
    assert 0 <= args.domain < 233
    assert args.count >= 0

    publisher_main(args.domain, args.count)
