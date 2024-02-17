; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @native_gates() local_unnamed_addr #0 {
entry:
  tail call void @__quantum__qis__zz__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0xC015FDBBE9BBA775, %Qubit* null)
  tail call void @__quantum__qis__u1q__body(double 0xC015FDBBE9BBA775, double 0xC015FDBBE9BBA775, %Qubit* null)
  tail call void @__quantum__qis__rzz__body(double 0xC015FDBBE9BBA775, %Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rxxyyzz__body(double 0xC015FDBBE9BBA775, double 0xC015FDBBE9BBA775, double 0x0, %Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  tail call void @__quantum__rt__result_record_output(%Result* null)
  ret void
}

declare void @__quantum__rt__result_record_output(%Result*) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*) local_unnamed_addr

declare void @__quantum__qis__zz__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__rz__body(double, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__rzz__body(double, %Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__rxxyyzz__body(double, double, double, %Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__u1q__body(double, double, %Qubit*) local_unnamed_addr


attributes #0 = { "EntryPoint" "requiredQubits"="2" "requiredResults"="1" }
